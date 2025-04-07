from pyrogram import Client, types
import requests
from configs.def_main import *

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
            "pais_codigo": data.get("country", {}).get("alpha2", "XX"),
            "pais_nombre": data.get("country", {}).get("name", "Desconocido") #agregado
        }
        return info_bin
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API de BINS: {e}")
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido",
                "pais_codigo": "XX", "pais_nombre": "Desconocido"}  # Retorna valores por defecto en caso de error
    except (ValueError, KeyError, TypeError) as e:
        print(f"Error al procesar la respuesta de la API: {e}")
        return {"banco": "Desconocido", "marca": "Desconocido", "tipo": "Desconocido", "pais": "Desconocido",
                "pais_codigo": "XX", "pais_nombre": "Desconocido"}



@ryas("bin")
async def bin_command(client: Client, message: types.Message):
    """
    Obtiene información sobre un BIN y la muestra formateada.
    """
    connection = None
    try:
        user_id = message.from_user.id
        username = message.from_user.username or "Usuario"

        connection, cursor = connect_db()
        cursor.execute("""
            SELECT rango, lang
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        user_data = cursor.fetchone()

        if not user_data:
            user_lang = message.from_user.language_code or 'es'
            if user_lang == 'en':
                from ryas_templates.chattext import en as text_dict
            else:
                from ryas_templates.chattext import es as text_dict
            await message.reply_text(text_dict['register_not'], reply_to_message_id=message.id)
            return

        rango = user_data[0]
        lang = user_data[1]

        if len(message.text.split()) < 2:
            if lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['bin_usage'], reply_to_message_id=message.id)
            return

        bin_prefix = message.text.split()[1]
        if len(bin_prefix) > 6:
            bin_prefix = bin_prefix[:6]

        bin_info = obtener_info_bin(bin_prefix)  # Llama a la función obtener_info_bin

        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        else:
            from ryas_templates.chattext import en as text_dict
        
        respuesta = text_dict['bin_message'].format(  # Usa el mensaje bin_message
            bin_prefix=bin_prefix,
            banco=bin_info.get('banco'), #posible error
            marca=bin_info.get('marca'),
            tipo=bin_info.get('tipo'),
            pais_nombre=bin_info.get('pais_nombre'), # Usar pais_nombre
            pais_codigo=bin_info.get('pais_codigo'),
            username=username,
            rango=rango,
            pais_emoji=bin_info['pais_codigo']
        )
        await message.reply_text(respuesta, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        await message.reply_text(f"Ocurrió un error al procesar el comando: {e}", reply_to_message_id=message.id)
    finally:
        if connection:
            cursor.close()
            connection.close()
