import random
import datetime
import requests
from configs.def_main import *
from pyrogram import Client, types
import re

# Función para generar números de tarjeta de crédito válida
def generar_tarjeta(bin_prefix, mes=None, anio=None, cvv_longitud=3):
    """
    Genera un número de tarjeta de crédito válido usando el algoritmo de Luhn.

    Parámetros:
        bin_prefix: Los primeros dígitos de la tarjeta (BIN).
        mes: Mes de expiración (opcional).
        anio: Año de expiración (opcional).
        cvv_longitud: Longitud del CVV (3 o 4 dígitos).

    Retorna:
        Una tupla con el número de tarjeta, mes, año de expiración y CVV.
    """
    bin_prefix = bin_prefix.replace('x', '')
    while len(bin_prefix) < 16:
        bin_prefix += str(random.randint(0, 9))

    suma = 0
    reversa_num = bin_prefix[::-1]
    for i, digito in enumerate(reversa_num):
        digito = int(digito)
        if i % 2 != 0:
            digito *= 2
            if digito > 9:
                digito -= 9
        suma += digito

    ultimo_digito = (10 - (suma % 10)) % 10
    numero_tarjeta = bin_prefix + str(ultimo_digito)

    if not mes:
        mes = random.randint(1, 12)
    if not anio:
        anio = random.randint(2024, 2030)
    if cvv_longitud == 3:
        cvv = str(random.randint(100, 999))
    elif cvv_longitud == 4:
        cvv = str(random.randint(1000, 9999))
    else:
        cvv = str(random.randint(100, 999))

    return numero_tarjeta, f"{mes:02d}", str(anio), cvv


# Función para obtener información del BIN usando una API
def obtener_info_bin(bin_prefix):
    """
    Obtiene información sobre el BIN (banco, marca, país) usando una API externa.

    Parámetros:
        bin_prefix: Los primeros 6 dígitos del número de tarjeta (BIN).

    Retorna:
        Un diccionario con la información del BIN, o None si no se encuentra.
    """
    try:
        # Usar una API de BINS pública
        url = f"https://bins.antipublic.cc/bins/{bin_prefix}"
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        data = response.json()
        # Extraer la información relevante
        info_bin = {
            "banco": data.get("bank", "Desconocido"),
            "marca": data.get("brand", "Desconocido"),
            "tipo": data.get("type", "Desconocido"),
            "pais": data.get("country", "Desconocido"),
            "pais_codigo": data.get("country_code", "XX"),
        }
        return info_bin
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API de BINS: {e}")
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido",
                "pais_codigo": "XX"}  # Retorna valores por defecto en caso de error
    except (ValueError, KeyError, TypeError) as e:
        print(f"Error al procesar la respuesta de la API: {e}")
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido",
                "pais_codigo": "XX"}



@ryas("gen")
async def gen_command(client: Client, message: types.Message):
    """
    Genera tarjetas de crédito falsas y muestra la información del BIN.

    Parámetros:
        client: El cliente del bot (por ejemplo, Telegram Bot API).
        message: El mensaje que activó el comando.
    """
    connection = None
    try:
        user_id = message.from_user.id
        connection, cursor = connect_db()

        cursor.execute("""
            SELECT rango, lang
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        user_data = cursor.fetchone()

        if not user_data:
            await message.reply("No estás registrado en la base de datos. Usa /register para registrarte.", reply_to_message_id=message.id)
            return

        rango = user_data[0]
        lang = user_data[1]
        username = message.from_user.username  # Obtén el nombre de usuario del objeto message

        parametros = message.text.split()[1:]  # Obtiene los parámetros del comando (.gen xxxx সম্ভাব্য)

        if not parametros:
            await message.reply("Uso: .gen bin|mm|aa|cvv o .gen bin|mm|aa o .gen bin", reply_to_message_id=message.id)
            return

        bin_prefix = parametros[0]
        mes = None
        anio = None
        cvv_longitud = 3  # Valor por defecto
        cvv = 'rnd'

        if len(parametros) > 1:
            fecha_parts = parametros[1].split('|')  # Usa split para separar
            if len(fecha_parts) >= 2:
                mes = fecha_parts[0]
                anio = fecha_parts[1]
            if len(fecha_parts) == 3:
                cvv = fecha_parts[2]  # Extract CVV
                if cvv.lower() == 'rnd':
                    cvv_longitud = random.choice([3, 4])
                else:
                    try:
                        cvv_longitud = int(cvv)
                        if cvv_longitud not in [3, 4]:
                            await message.reply("CVV debe ser 3, 4 o 'rnd'", reply_to_message_id=message.id)
                            return
                    except ValueError:
                        await message.reply("CVV debe ser 3, 4 o 'rnd'", reply_to_message_id=message.id)
                        return
            elif len(fecha_parts) > 3:
                await message.reply("Formato incorrecto. Use .gen bin|mm|aa|cvv", reply_to_message_id=message.id)
                return
        elif len(parametros) == 1:
            pass  # No hacer nada si solo se proporciona el BIN
        else:
            await message.reply("Formato incorrecto. Use .gen bin|mm|aa|cvv o .gen bin|mm|aa o .gen bin", reply_to_message_id=message.id)
            return


        if len(bin_prefix) < 6:
            await message.reply("El BIN debe tener al menos 6 dígitos.", reply_to_message_id=message.id)
            return

        info_bin = obtener_info_bin(bin_prefix[:6])  # Obtener info del BIN de los primeros 6 dígitos
        
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        else:
            from ryas_templates.chattext import en as text_dict

        tarjetas = []
        for _ in range(10):
            try:
                gen_mes = int(mes) if mes else None
                gen_anio = int(anio) if anio else None
                numero_tarjeta, gen_mes_str, gen_anio_str, cvv_gen = generar_tarjeta(bin_prefix, gen_mes, gen_anio, cvv_longitud)
                tarjetas.append(f"{numero_tarjeta}|{gen_mes_str}|{gen_anio_str}|{cvv_gen}")
            except ValueError as e:
                await message.reply(f"Error al generar tarjeta: {e}", reply_to_message_id=message.id)
                return
        
        respuesta = text_dict['gen_response'].format(
            bin_prefix=bin_prefix[:6],
            banco=info_bin['banco'],
            marca=info_bin['marca'],
            tipo=info_bin['tipo'],
            pais=info_bin['pais'],
            pais_codigo=info_bin['pais_codigo'],
            tarjetas="\n".join(tarjetas),
            username=username,
            rango=rango
        )

        await message.reply_text(respuesta, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        await message.reply_text(f"Ocurrió un error al procesar el comando: {e}", reply_to_message_id=message.id)
    finally:
        if connection:
            cursor.close()
            connection.close()
