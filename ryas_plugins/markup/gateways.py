from configs.def_main import *


@ryasbt("^gateways$")
async def gateways_markup(client: Client, callback_query: types.CallbackQuery):
    """
    Muestra el menú de gateways al tocar el markup correspondiente.

    Args:
        client: El objeto Client de Pyrogram.
        callback_query: El objeto CallbackQuery de Pyrogram que activó el markup.
    """
    user_id = callback_query.from_user.id
    connection, cursor = connect_db()
    cursor.execute("SELECT lang FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    lang = result[0] if result else 'es'

    # Cargar el texto y los botones en el idioma correspondiente
    if lang == 'es':
        from ryas_templates.chattext import es as text_dict
        from ryas_templates.botones import es as botones_dict  # Asegúrate de que este archivo exista
    elif lang == 'en':
        from ryas_templates.chattext import en as text_dict
        from ryas_templates.botones import en as botones_dict  # Asegúrate de que este archivo exista
    else:
        from ryas_templates.chattext import es as text_dict  # Por defecto español
        from ryas_templates.botones import es as botones_dict  # Por defecto español

    await callback_query.message.edit_text(
        text=text_dict['gatesx_message'],
        reply_markup=botones_dict['gatewaysx']
    )
