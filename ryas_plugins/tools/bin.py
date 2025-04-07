from pyrogram import Client, types
import requests
from configs.def_main import *
from func_bin import get_bin_info  # Importa la función get_bin_info

@ryas("bin")
async def bin_command(client: Client, message: types.Message):
    """
    Obtiene información sobre un BIN y la muestra formateada.

    Parámetros:
        client: El cliente del bot (por ejemplo, Telegram Bot API).
        message: El mensaje que activó el comando.
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

        bin_info = get_bin_info(bin_prefix)  # Llama a la función get_bin_info

        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        else:
            from ryas_templates.chattext import en as text_dict
        
        # Verificar si la información del BIN se obtuvo correctamente
        if bin_info:
            respuesta = text_dict['bin_message'].format(  # Usa el mensaje bin_message
                bin_prefix=bin_prefix,
                banco=bin_info.get('banco'),  # Usa .get() para evitar errores si la clave no existe
                marca=bin_info.get('marca'),
                tipo=bin_info.get('tipo'),
                pais_nombre=bin_info.get('pais_nombre'),  # Usa pais_nombre
                pais_codigo=bin_info['pais_codigo'],
                username=username,
                rango=rango,
                pais_emoji=bin_info.get('pais_codigo', '')
            )
        else:
            respuesta = f"No se pudo obtener información del BIN {bin_prefix}."

        await message.reply_text(respuesta, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        await message.reply_text(f"Ocurrió un error al procesar el comando: {e}", reply_to_message_id=message.id)
    finally:
        if connection:
            cursor.close()
            connection.close()
