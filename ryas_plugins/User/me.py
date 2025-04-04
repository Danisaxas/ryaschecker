from configs.def_main import *
from pyrogram import Client, types

# Decorador para el comando "me"
@ryas('me')
async def me_command(client: Client, message: types.Message):
    """
    Muestra la información del usuario que usa el comando, en su idioma.

    Parámetros:
        client: El cliente del bot (ej., Telegram Bot API).
        message: El mensaje que activó el comando.
    """
    user_id = message.from_user.id
    connection = None
    try:
        connection, cursor = connect_db()

        # Obteniendo el idioma del usuario de la base de datos
        cursor.execute("""
            SELECT rango, creditos, antispam, expiracion, lang
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        user_data = cursor.fetchone()

        if not user_data:
            # Si el usuario no está registrado, obtener el idioma del mensaje
            user_lang = message.from_user.language_code or 'es' #por defecto español
            if user_lang.startswith('en'):
                user_lang = 'en'
            else:
                user_lang = 'es'
            if user_lang == 'en':
                from ryas_templates.chattext import en as text_dict
            else:
                from ryas_templates.chattext import es as text_dict
            await message.reply_text(en['register_not'] if user_lang == 'en' else es['register_not'], reply_to_message_id=message.id)
            return

        rango, creditos, antispam, expiration, lang = user_data
        username = message.from_user.username or "Usuario"

        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict #por defecto español

        # Formatear el mensaje de respuesta con la información del usuario
        formatted_text = text_dict['metext'].format(
            username=username,
            user_id=user_id,
            firts_name=message.from_user.first_name,  # Corrección: first_name
            rango=rango,
            creditos=creditos,
            antispam=antispam,
            expiration=expiration or 'No expiration'
        )
        await message.reply_text(formatted_text, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Error en me_command: {e}")
        await message.reply_text(
            "Ocurrió un error al procesar el comando me.",
            reply_to_message_id=message.id
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
