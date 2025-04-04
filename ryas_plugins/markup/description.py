from configs.def_main import *
from pyrogram import Client, types

@ryasbt("^description$")
async def description_callback(client: Client, callback_query: types.CallbackQuery):
    """
    Muestra la descripción del bot en el idioma del usuario.
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
            text_dict['description_text'],
            reply_markup=back
        )
    except Exception as e:
        print(f"Error en description_callback: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=None
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
