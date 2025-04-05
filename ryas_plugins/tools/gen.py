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
            SELECT rango
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        user_data = cursor.fetchone()

        if not user_data:
            await message.reply("No estás registrado en la base de datos. Usa /register para registrarte.", reply_to_message_id=message.id)
            return

        rango = user_data[0]
        username = message.from_user.username  # Obtén el nombre de usuario del objeto message
        
        input_text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ""

        input_parts = input_text.split('|')
        cc_input = input_parts[0]
        mes = None
        anio = None
        cvv_longitud = 3  # Valor por defecto

        if len(input_parts) > 1:
            mes = input_parts[1]
        if len(input_parts) > 2:
            anio = input_parts[2]
        if len(input_parts) > 3:
            cvv_longitud = input_parts[2]
            if cvv_longitud.lower() == 'rnd':
                cvv_longitud = random.choice([3, 4])
            else:
                try:
                    cvv_longitud = int(cvv_longitud)
                    if cvv_longitud not in [3, 4]:
                        await message.reply("CVV debe ser 3, 4 o 'rnd'", reply_to_message_id=message.id)
                        return
                except ValueError:
                    await message.reply("CVV debe ser 3, 4 o 'rnd'", reply_to_message_id=message.id)
                    return
        elif len(input_parts) == 1:
            pass  # No hacer nada si solo se proporciona el BIN
        elif len(input_parts) == 2:
            mes, anio = input_parts[1].split('|')
        

        if len(cc_input) < 6:
            await message.reply("El BIN debe tener al menos 6 dígitos.", reply_to_message_id=message.id)
            return

        info_bin = obtener_info_bin(cc_input[:6])

        respuesta = "💳 Tus Tarjetas Generadas 💳\n"
        respuesta += "- - - - - - - - - - - - - - - - - - - - - - -\n"
        respuesta += f"BIN: {cc_input[:6]}\n"
        respuesta += "- - - - - - - - - - - - - - - - - - - - - - -\n"
        respuesta += f"Banco: {info_bin['banco']}\n"
        respuesta += f"Marca: {info_bin['marca']}\n"
        respuesta += f"Tipo: {info_bin['tipo']}\n"
        respuesta += f"País: {info_bin['pais']} ({info_bin['pais_codigo']})\n"
        respuesta += "- - - - - - - - - - - - - - - - - - - - - - -\n\n"

        for _ in range(10):
            try:
                gen_mes = int(mes) if mes else None
                gen_anio = int(anio) if anio else None
                numero_tarjeta, gen_mes_str, gen_anio_str, cvv = generar_tarjeta(cc_input, gen_mes, gen_anio, cvv_longitud)
                respuesta += f"{numero_tarjeta}|{gen_mes_str}|{gen_anio_str}|{cvv}\n"
            except ValueError as e:
                await message.reply(f"Error al generar tarjeta: {e}", reply_to_message_id=message.id)
                return

        respuesta += f"\nReq By: @{username}[{rango}]"

        await message.reply(respuesta, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        await message.reply(f"Ocurrió un error al procesar el comando: {e}", reply_to_message_id=message.id)
    finally:
        if connection:
            cursor.close()
            connection.close()
