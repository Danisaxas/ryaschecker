import random
import datetime
import requests
import time
from configs.def_main import *

# Función para generar números de tarjeta
def cc_gen(cc, mes, ano, cvv):
    """
    Genera las partes de la tarjeta de ejemplo. Aquí puedes incluir tu lógica de generación.
    """
    return (f"{cc[:4]} XXXX XXXX XXXX", f"{cc[4:8]} XXXX XXXX XXXX", f"{cc[8:12]} XXXX XXXX XXXX", f"{cc[12:16]} XXXX XXXX XXXX",
            f"{cc[:4]} XXXX XXXX XXXX", f"{cc[4:8]} XXXX XXXX XXXX", f"{cc[8:12]} XXXX XXXX XXXX", f"{cc[12:16]} XXXX XXXX XXXX",
            f"{cc[:4]} XXXX XXXX XXXX", f"{cc[4:8]} XXXX XXXX XXXX")

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
        cc = input_parts[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'

        if len(input_parts) > 1:
            mes = input_parts[1]
        if len(input_parts) > 2:
            ano = input_parts[2]
        if len(input_parts) > 3:
            cvv = input_parts[3]
            
        if len(cc) < 6:
            await message.reply("El BIN debe tener al menos 6 dígitos.", reply_to_message_id=message.id)
            return

        bin_info = obtener_info_bin(cc[:6])
        
        tiempoinicio = time.perf_counter()
        cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = cc_gen(cc, mes, ano, cvv)
        tiempofinal = time.perf_counter()

        text = f"""
𝑳𝒖𝒙𝑪𝒉𝒆𝒌𝒆𝒓 𝑪𝑪 𝑮𝒆𝒏
━━━━━━━━
<code>{cc1}</code>
<code>{cc2}</code>
<code>{cc3}</code>
<code>{cc4}</code>
<code>{cc5}</code>
<code>{cc6}</code>
<code>{cc7}</code>
<code>{cc8}</code>
<code>{cc9}</code>
<code>{cc10}</code>
━━━━━━━━
𝘽𝙞𝙣: <code>{cc[:6]}</code>
𝙄𝙣𝙛𝙤: {bin_info.get("marca", "Desconocido")} - {bin_info.get("tipo", "Desconocido")} - {bin_info.get("level", "Desconocido")}
𝘽𝙖𝙣𝙠: <code>{bin_info.get("banco", "Desconocido")} {bin_info.get("pais_codigo", "XX")}</code>
𝙂𝙚𝙣 𝙗𝙮: <code>@{message.from_user.username} [{rango}]</code>
"""

        await client.send_message(
            message.chat.id,
            text,
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton("𝗥𝗘-𝗚𝗘𝗡", callback_data="gen_pro")
                    ]
                ]
            ),
            disable_web_page_preview=True
        )

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        await message.reply(f"Ocurrió un error al procesar el comando: {e}", reply_to_message_id=message.id)
    finally:
        if connection:
            cursor.close()
            connection.close()
