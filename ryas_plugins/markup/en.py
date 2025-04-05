# markup/en.py
from configs.def_main import *
from pyrogram import Client, types

@ryasbt("^en$")
async def handle_en_button(client: Client, callback_query: types.CallbackQuery):
    """
    Actualiza el idioma del usuario a inglés ("en") en la base de datos y muestra un mensaje de confirmación.
    """
    connection = None
    try:
        # Conecta a la base de datos usando la función connect_db()
        connection, cursor = connect_db()

        # Actualiza el idioma del usuario en la tabla 'users'
        user_id = callback_query.from_user.id
        update_query = "UPDATE users SET lang = 'en' WHERE user_id = %s"
        cursor.execute(update_query, (user_id,))
        connection.commit()

        # Cargar los botones en el idioma correspondiente
        from ryas_templates.botones import en as botones_dict

        # Responde al usuario con un mensaje de confirmación y el teclado 'back'
        await callback_query.message.edit_text(
            "Your language has been set to English 🇺🇸",
            reply_markup=botones_dict['back']  # Usa el teclado del idioma correspondiente
        )

    except Exception as e:
        # Maneja errores
        await callback_query.message.edit_text(
            f"An error occurred: {e}",
            reply_markup=None
        )
    finally:
        # Asegura que la conexión se cierre
        if connection:
            cursor.close()
            connection.close()
