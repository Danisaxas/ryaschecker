from pyrogram import Client, types
import requests
from configs.def_main import *
from func_bin import get_bin_info # Importa la función get_bin_info desde func_bin.py
import sqlite3
import random

def luhn_verification(num):
    """
    Verifica si un número de tarjeta de crédito es válido según el algoritmo de Luhn.
    """
    num = [int(d) for d in str(num)]
    check_digit = num.pop()
    num.reverse()
    total = 0
    for i, digit in enumerate(num):
        if i % 2 == 0:
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        total += digit
    total = total * 9
    return (total % 10) == check_digit

def cc_gen(bin_prefix, mes='rnd', ano='rnd', cvv='rnd'):
    """
    Genera una tarjeta de crédito válida usando el algoritmo de Luhn.

    Args:
        bin_prefix (str): Los primeros dígitos del BIN (6 o 12).
        mes (str, opcional): El mes de expiración (MM) o 'rnd' para aleatorio.
        ano (str, opcional): El año de expiración (AAAA) o 'rnd' para aleatorio.
        cvv (str, opcional): El CVV (3 o 4 dígitos) o 'rnd' para aleatorio.

    Returns:
        str: La tarjeta de crédito generada con el formato CC|MM|AAAA|CVV, o None si falla.
    """
    card_length = 16 if bin_prefix[0] != '3' else 15
    remaining_digits = card_length - len(bin_prefix)
    
    for _ in range(100): # Intentar generar una tarjeta válida hasta 100 veces
        card_number = bin_prefix + "".join(random.choice("0123456789") for _ in range(remaining_digits))
        if luhn_verification(card_number):
            break
    else:
        return None  # No se pudo generar una tarjeta válida

    if mes == 'rnd':
        mes_gen = random.randint(1, 12)
        mes_gen_str = f"{mes_gen:02d}"  # Asegura que el mes tenga dos dígitos
    else:
        mes_gen_str = mes
    
    if ano == 'rnd':
        ano_gen = random.randint(2023, 2031)
    else:
        ano_gen = int(ano)
    ano_gen_str = str(ano_gen)

    if cvv == 'rnd':
        cvv_len = 4 if card_number[0] == '3' else 3
        cvv_gen_str = "".join(random.choice("0123456789") for _ in range(cvv_len))
    else:
        cvv_gen_str = cvv
    
    return f"{card_number}|{mes_gen_str}|{ano_gen_str}|{cvv_gen_str}"

@ryas("gen")
async def gen_command(client: Client, message: types.Message):
    """
    Genera tarjetas de crédito falsas basadas en un BIN proporcionado.

    Args:
        client: El objeto Client de Pyrogram para interactuar con Telegram.
        message: El objeto Message de Pyrogram que contiene el comando y el BIN.
    """
    connection = None
    cursor = None
    try:
        connection, cursor = connect_db()
        user_id = message.from_user.id

        # Obtener información del usuario (rango, idioma) desde la base de datos
        cursor.execute("""
            SELECT rango, lang
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            rango_usuario, lang_usuario = user_data
        else:
            rango_usuario = "Free"  # Valor por defecto si no se encuentra el usuario
            lang_usuario = "es"  # Valor por defecto

        # Cargar el texto en el idioma correspondiente
        if lang_usuario == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang_usuario == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict  # Por defecto español

        # Extraer los argumentos del comando
        parts = message.text.split()
        if len(parts) < 2:
            await message.reply_text("Por favor, proporciona un BIN válido después del comando .gen", reply_to_message_id=message.id)
            return

        bin_arg = parts[1]
        fecha_arg = "rnd"
        cvv_arg = "rnd"

        if len(parts) > 2:
            fecha_arg = parts[2]
        if len(parts) > 3:
            cvv_arg = parts[3]

        bin_number = bin_arg.replace("x", "")[:6]  # Obtener los primeros 6 dígitos del BIN

        # Validar que el BIN tenga al menos 6 dígitos
        if len(bin_number) < 6:
            await message.reply_text("El BIN debe tener al menos 6 dígitos.", reply_to_message_id=message.id)
            return

        # Generar las tarjetas de crédito
        generated_cards = [cc_gen(bin_arg, mes=fecha_arg, ano=fecha_arg, cvv=cvv_arg) for _ in range(10)]
        generated_cards = [card for card in generated_cards if card is not None] #quita Nones

        if not generated_cards:
            await message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", reply_to_message_id=message.id)
            return

        # Obtener información del BIN para mostrar en el mensaje
        bin_info = get_bin_info(bin_number) # Obtiene la info del BIN del diccionario cargado desde el CSV
        if bin_info:
            banco = bin_info['bank_name']
            marca = bin_info['vendor']
            tipo = bin_info['type']
            pais = bin_info['country']
            pais_codigo = bin_info['iso']
            bandera = bin_info['flag']
        else:
            banco = "Desconocido"
            marca = "Desconocido"
            tipo = "Desconocido"
            pais = "Desconocido"
            pais_codigo = "Desconocido"
            bandera = ""

        # Formatear el mensaje de respuesta
        tarjetas_formateadas = "\n".join(f"-{card.strip()}-" for card in generated_cards)  # Unir las tarjetas generadas en un solo string

        respuesta = text_dict['gen_response'].format(  # Usar el mensaje predefinido
            bin_prefix=bin_number,
            banco=banco,
            marca=marca,
            tipo=tipo,
            pais=pais,
            pais_codigo=pais_codigo,
            tarjetas=tarjetas_formateadas,
            username=message.from_user.username or message.from_user.first_name or "Usuario",
            rango=rango_usuario,
            bandera=bandera
        )

        await message.reply_text(respuesta, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Error en gen_command: {e}")
        await message.reply_text(
            "Ocurrió un error al procesar el comando gen.",
            reply_to_message_id=message.id
        )
    finally:
        if connection:
            connection.close()
