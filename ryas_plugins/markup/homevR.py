from configs.def_main import *
from pyrogram import Client, types

@ryasbt("^homevR$")
async def handle_homevr_button(client: Client, callback_query: types.CallbackQuery):
    connection = None
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username or "Usuario"

        connection, cursor = connect_db()
        cursor.execute("SELECT lang FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'

        if lang == 'es':
            from ryas_templates.botones import es as botones_dict
            from ryas_templates.chattext import es as text_dict
            idioma_actual = "🇪🇸"
        elif lang == 'en':
            from ryas_templates.botones import en as botones_dict
            from ryas_templates.chattext import en as text_dict
            idioma_actual = "🇺🇸"
        else:
            from ryas_templates.botones import es as botones_dict
            from ryas_templates.chattext import es as text_dict
            idioma_actual = "🇪🇸"

        await callback_query.message.edit_text(
            text=text_dict['ryas_cloud'].format(username=username),
            reply_markup=botones_dict['vryasx']
        )

    except Exception as e:
        print(f"Error en handle_homevr_button: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=None
        )
    finally:
        if connection:
            cursor.close()
            connection.close()