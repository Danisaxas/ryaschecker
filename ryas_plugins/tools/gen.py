import random
import datetime
import requests  # Para hacer la solicitud a la API de BINS
from configs.def_main import * # Importando configuraciones

# Función para generar una tarjeta de crédito válida
def generar_tarjeta(bin_prefix, mes=None, anio=None):
    """
    Genera un número de tarjeta de crédito válido usando el algoritmo de Luhn.

    Parámetros:
        bin_prefix: Los primeros dígitos de la tarjeta (BIN).
        mes: Mes de expiración (opcional).
        anio: Año de expiración (opcional).

    Retorna:
        Una tupla con el número de tarjeta, mes y año de expiración.
        Si no se proporciona mes o año, se generan aleatoriamente.
    """
    while len(bin_prefix) < 15:
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
        anio = random.randint(2024, 2030)  # Años de expiración razonables

    return numero_tarjeta, f"{mes:02d}", str(anio)


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
        # Usar una API de BINS pública (¡Cambiar por una confiable!)
        url = f"https://lookup.binlist.net/{bin_prefix}"  # Ejemplo de API
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        data = response.json()
        # Extraer la información relevante
        info_bin = {
            "banco": data.get("bank", {}).get("name", "Desconocido"),
            "marca": data.get("scheme", "Desconocido"),
            "tipo": data.get("type", "Desconocido"),
            "pais": data.get("country", {}).get("name", "Desconocido"),
            "pais_codigo": data.get("country", {}).get("alpha2", "XX"),  # Obtener el código del país
        }
        return info_bin
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API de BINS: {e}")
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido", "pais_codigo": "XX"}  # Retorna valores por defecto en caso de error
    except (ValueError, KeyError, TypeError) as e:
        print(f"Error al procesar la respuesta de la API: {e}")
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido", "pais_codigo": "XX"}

@ryas("gen")
async def gen_command(client, message):
    """
    Genera tarjetas de crédito falsas y muestra la información del BIN.

    Parámetros:
        client: El cliente del bot (por ejemplo, Telegram Bot API).
        message: El mensaje que activó el comando.
    """
    try:
        user_id = message.from_user.id
        connection, cursor = connect_db()

        cursor.execute("""
            SELECT rango, username
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        user_data = cursor.fetchone()

        if not user_data:
            await message.reply("Usuario no encontrado en la base de datos.", reply_to_message_id=message.id)
            return

        rango, username = user_data
        parametros = message.text.split()[1:]  # Obtiene los parámetros del comando (.gen xxxx yyyy)

        if not parametros:
            await message.reply("Uso: .gen bin|mm|aa", reply_to_message_id=message.id)
            return

        bin_prefix = parametros[0]
        mes = None
        anio = None

        if len(parametros) > 1:
            fecha_parts = parametros[1].split(
                ':'
            )  # Usa split para separar por :, / o |
            if len(fecha_parts) == 2:
                mes, anio = fecha_parts
            elif len(fecha_parts) == 1:
                mes = fecha_parts[0]

        if len(parametros) > 2:
            anio = parametros[2]

        if len(bin_prefix) < 6:
            await message.reply("El BIN debe tener al menos 6 dígitos.", reply_to_message_id=message.id)
            return

        info_bin = obtener_info_bin(bin_prefix[:6])  # Obtener info del BIN de los primeros 6 dígitos

        respuesta = "💳 Tus Tarjetas Generadas 💳\n"
        respuesta += "- - - - - - - - - - - - - - - - - - - - - - -\n"
        respuesta += f"BIN: {bin_prefix}\n"
        respuesta += "- - - - - - - - - - - - - - - - - - - - - - -\n"
        respuesta += f"Banco: {info_bin['banco']}\n"
        respuesta += f"Marca: {info_bin['marca']}\n"  # Agregado Marca
        respuesta += f"Tipo: {info_bin['tipo']}\n"
        respuesta += f"País: {info_bin['pais']} ({info_bin['pais_codigo']})\n"
        respuesta += "- - - - - - - - - - - - - - - - - - - - - - -\n\n"

        for _ in range(10):
            numero_tarjeta, gen_mes, gen_anio = generar_tarjeta(bin_prefix, mes, anio)
            respuesta += f"{numero_tarjeta}|{gen_mes}|{gen_anio}|{random.randint(100, 999)}\n"  # Agregado CVV

        respuesta += f"\nReq By: @{username}[{rango}]"  # Información del solicitante

        await message.reply(respuesta, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        await message.reply(f"Ocurrió un error al procesar el comando: {e}", reply_to_message_id=message.id)
