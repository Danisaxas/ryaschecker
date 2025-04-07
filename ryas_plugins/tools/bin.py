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

        bin_info = get_bin_info(bin_prefix[:6])  # Llama a la función get_bin_info

        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        else:
            from ryas_templates.chattext import en as text_dict

        respuesta = text_dict['bin_message'].format(  # Usa el mensaje bin_message
            flag=bin_info.get('pais_codigo', 'XX'), # Obtiene la bandera del país
            bin=bin_prefix,
            bank=bin_info.get('banco', "Desconocido"),  
            level=bin_info.get('level', "Desconocido"),
            vendor=bin_info.get('marca', "Desconocido"),
            type=bin_info.get('tipo', "Desconocido"),
            country=bin_info.get('pais_nombre', "Desconocido"),  # Usa pais_nombre
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
