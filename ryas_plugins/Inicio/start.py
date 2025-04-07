# ryas_plugins/inicio/start.py
from configs.def_main import *
import pytz
from datetime import datetime
from pyrogram import Client, types

@ryas("start")
async def start(client: Client, message: types.Message):
    """
    Muestra el mensaje de inicio en el idioma del usuario.
    """
    user_id = message.from_user.id
    connection = None
    try:
        connection, cursor = connect_db()

        cursor.execute("""
            SELECT rango, creditos, antispam, expiracion, lang, ban, razon
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        user_data = cursor.fetchone()

        if not user_data:
            # Obtener el idioma del usuario del mensaje
            user_lang = message.from_user.language_code or 'es'  # por defecto español
            if user_lang.startswith('en'):
                user_lang = 'en'
            else:
                user_lang = 'es'
            if user_lang == 'en':
                from ryas_templates.chattext import en as text_dict
                from ryas_templates.botones import en as botones_dict
            else:
                from ryas_templates.chattext import es as text_dict
                from ryas_templates.botones import es as botones_dict
            await message.reply_text(en['register_not'] if user_lang == 'en' else es['register_not'], reply_to_message_id=message.id)
            return

        rango, creditos, antispam, expiracion, lang, ban, razon = user_data
        username = message.from_user.username or "Usuario"
        caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")

        # Cargar el texto y los botones en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
            from ryas_templates.botones import es as botones_dict
            idioma_actual = "🇪🇸"
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
            from ryas_templates.botones import en as botones_dict
            idioma_actual = "🇺🇸"
        else:
            from ryas_templates.chattext import es as text_dict  # por defecto español
            from ryas_templates.botones import es as botones_dict
            idioma_actual = "🇪🇸"

        response = text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=caracas_time) #agregado idioma_actual

        await message.reply_text(
            response,
            reply_to_message_id=message.id,
            reply_markup=botones_dict['mainstart']  # Usa el teclado del idioma correspondiente
        )

    except Exception as e:
        print(f"Error en start: {e}")
        await message.reply_text(
            "Ocurrió un error al procesar el comando start.",
            reply_to_message_id=message.id
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
