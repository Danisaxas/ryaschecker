import random
import datetime
import requests  # Para hacer la solicitud a la API de BINS
from configs.def_main import * # Importando configuraciones

# Función para generar una tarjeta de crédito válida
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
    bin_prefix = bin_prefix.replace('x', '')  # Elimina todas las 'x'
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
        anio = random.randint(2024, 2030)  # Años de expiración razonables
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
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido",
                "pais_codigo": "XX"}  # Retorna valores por defecto en caso de error
    except (ValueError, KeyError, TypeError) as e:
        print(f"Error al procesar la respuesta de la API: {e}")
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido",
                "pais_codigo": "XX"}



@ryas("gen")
async def gen_command(client, message):
    """
    Genera tarjetas de crédito falsas y muestra la información del BIN.

    Parámetros:
        client: El cliente del bot (por ejemplo, Telegram Bot API).
        message: El mensaje que activó el comando.
    """
    connection = None # Initialize connection
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
            await message.reply("Usuario no encontrado en la base de datos.", reply_to_message_id=message.id)
            return

        rango = user_data[0]
        username = message.from_user.username  # Obtén el nombre de usuario del objeto message

        parametros = message.text.split()[1:]  # Obtiene los parámetros del comando (.gen xxxx সম্ভাব্য)

        if not parametros:
            await message.reply("Uso: .gen bin|mm|aa|rnd", reply_to_message_id=message.id)
            return

        bin_prefix = parametros[0]
        mes = None
        anio = None
        cvv_longitud = 3  # Valor por defecto

        if len(parametros) > 1:
            fecha_parts = parametros[1].split('|')  # Usa split para separar por |
            if len(fecha_parts) == 2:
                mes, anio = fecha_parts
            elif len(fecha_parts) == 3:  # añadido
                mes, anio, cvv_longitud_str = fecha_parts
                try:
                    cvv_longitud = int(cvv_longitud_str)
                except ValueError:
                    await message.reply("El CVV debe ser 3, 4 o 'rnd'.", reply_to_message_id=message.id)
                    return
            else:
                await message.reply("Formato de fecha incorrecto. Use mm|aa o mm|aa|cvv.", reply_to_message_id=message.id)
                return

        if len(parametros) > 2:
            anio = parametros[2]
        
        if len(parametros) > 3:
            if parametros[3].lower() == 'rnd':
                cvv_longitud = random.choice([3, 4])
            else:
                try:
                    cvv_longitud = int(parametros[3])
                except ValueError:
                    await message.reply("El CVV debe ser 3, 4 o 'rnd'.", reply_to_message_id=message.id)
                    return

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
            try:
                # Intenta convertir mes y anio a enteros, maneja el error si no son válidos
                gen_mes = int(mes) if mes else None
                gen_anio = int(anio) if anio else None
                numero_tarjeta, gen_mes_str, gen_anio_str, cvv = generar_tarjeta(bin_prefix, gen_mes, gen_anio, cvv_longitud)
                respuesta += f"{numero_tarjeta}|{gen_mes_str}|{gen_anio_str}|{cvv}\n"  # Agregado CVV
            except ValueError as e:
                await message.reply(f"Error al generar tarjeta: {e}", reply_to_message_id=message.id)
                return

        respuesta += f"\nReq By: @{username}[{rango}]"  # Información del solicitante

        await message.reply(respuesta, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        await message.reply(f"Ocurrió un error al procesar el comando: {e}", reply_to_message_id=message.id)
    finally:
        if connection:
            cursor.close()
            connection.close()
