from configs.def_main import *
from pyrogram import Client, types
import pytz
from datetime import datetime

@ryasbt("^tools$")
async def tools_callback(client: Client, callback_query: types.CallbackQuery):
    """
    Muestra las herramientas disponibles, en el idioma del usuario.
    """
    user_id = callback_query.from_user.id
    connection = None
    try:
        connection, cursor = connect_db()
        cursor.execute("SELECT lang FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'

        # Cargar el texto y los botones en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
            from ryas_templates.botones import es as botones_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
            from ryas_templates.botones import en as botones_dict
        else:
            from ryas_templates.chattext import es as text_dict  # Por defecto español
            from ryas_templates.botones import es as botones_dict

        await callback_query.message.edit_text(
            text_dict['tools'],
            reply_markup=botones_dict['atras']  # Usa el teclado del idioma correspondiente
        )
    except Exception as e:
        print(f"Error en tools_callback: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=None
        )
    finally:
        if connection:
            cursor.close()
            connection.close()


