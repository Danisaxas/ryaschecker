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

        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict #por defecto español

        await callback_query.message.edit_text(
            text_dict['tools'],
            reply_markup=atras
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

@ryasbt("^home$")
async def home_callback(client: Client, callback_query: types.CallbackQuery):
    """
    Muestra el mensaje de inicio, en el idioma del usuario.
    """
    user_id = callback_query.from_user.id
    connection = None
    try:
        connection, cursor = connect_db()
        cursor.execute("SELECT lang FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'

        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict #por defecto español
        
        username = callback_query.from_user.username or "Usuario"
        caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")

        await callback_query.message.edit_text(
            text_dict['startx'].format(username=username, caracas_time=caracas_time),
            reply_markup=mainstart
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

