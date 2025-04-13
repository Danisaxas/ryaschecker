from configs.def_main import *
from pyrogram import Client, types
import pytz
from datetime import datetime

@ryasbt("^home$")
async def home_callback(client: Client, callback_query: types.CallbackQuery):
    """
    Muestra el mensaje de inicio, en el idioma del usuario.
    """
    connection = None
    try:
        user_id = callback_query.from_user.id
        connection, cursor = connect_db()
        cursor.execute("SELECT lang FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'

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
            from ryas_templates.chattext import es as text_dict  # Por defecto español
            from ryas_templates.botones import es as botones_dict
            idioma_actual = "🇪🇸"
        
        username = callback_query.from_user.username or "Usuario"
        caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")

        await callback_query.message.edit_text(
            text=text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=caracas_time), #agregado idioma_actual
            reply_markup=botones_dict['mainstart'] # Usa el teclado del idioma correspondiente
        )
    except Exception as e:
        print(f"Error en home_callback: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=None
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
