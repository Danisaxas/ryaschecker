# markup/es.py
from configs.def_main import *
from pyrogram import Client, types
import pytz
from datetime import datetime

@ryasbt("^es$")
async def handle_es_button(client: Client, callback_query: types.CallbackQuery):
    """
    Actualiza el idioma del usuario a español ("es") en la base de datos y muestra el menú de inicio.
    """
    connection = None
    try:
        # Conecta a la base de datos
        connection, cursor = connect_db()

        # Actualiza el idioma del usuario en la tabla 'users'
        user_id = callback_query.from_user.id
        update_query = "UPDATE users SET lang = 'es' WHERE user_id = %s"
        cursor.execute(update_query, (user_id,))
        connection.commit()

        # Cargar el texto en el idioma correspondiente
        from ryas_templates.chattext import es as text_dict

        username = callback_query.from_user.username or "Usuario"
        caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")

        # Muestra el menú de inicio
        await callback_query.message.edit_text(
            text_dict['startx'].format(username=username, caracas_time=caracas_time),
            reply_markup=mainstart
        )

    except Exception as e:
        print(f"Error en handle_es_button: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=None
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
