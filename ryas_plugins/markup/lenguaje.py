from configs.def_main import *
from pyrogram import Client, types

@ryasbt("^lenguaje$")
async def handle_lenguaje_button(client: Client, callback_query: types.CallbackQuery):
    """
    Muestra el menú de idiomas disponibles.
    """
    connection = None
    try:
        user_id = callback_query.from_user.id

        # Obtener el idioma del usuario desde la base de datos
        connection, cursor = connect_db()
        cursor.execute("SELECT lang FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'  # Default to 'es' if not found

        # Cargar los botones en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.botones import es as botones_dict
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.botones import en as botones_dict
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.botones import es as botones_dict  # Por defecto español
            from ryas_templates.chattext import es as text_dict

        await callback_query.message.edit_text(
            text=text_dict['lang_message'].format(idioma_actual=lang.capitalize()),
            reply_markup=botones_dict['lang']  # Usa el teclado del idioma correspondiente
        )
    except Exception as e:
        print(f"Error en handle_lenguaje_button: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=None
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
