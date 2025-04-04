# markup/en.py
from configs.def_main import * # Importa todo desde configs.def_main

@ryasbt("^en$")
async def handle_en_button(client: Client, callback_query: types.CallbackQuery):
    """
    Actualiza el idioma del usuario a inglés ("en") en la base de datos.
    """
    try:
        # Conecta a la base de datos usando la función connect_db()
        connection, cursor = connect_db()

        # Actualiza el idioma del usuario en la tabla 'users'
        user_id = callback_query.from_user.id
        update_query = "UPDATE users SET lang = 'en' WHERE user_id = %s"
        cursor.execute(update_query, (user_id,))
        connection.commit()

        # Responde al usuario
        await callback_query.message.edit_text(
            "Your language has been set to English.",  # Mensaje en inglés
            reply_markup=None  # Elimina el teclado anterior
        )

    except mysql.connector.Error as e:
        # Maneja errores de la base de datos
        await callback_query.message.edit_text(
            f"Database error: {e}",
            reply_markup=None
        )
    except Exception as e:
        # Maneja otros errores
        await callback_query.message.edit_text(
            f"An error occurred: {e}",
            reply_markup=None
        )
    finally:
        # Asegura que la conexión se cierre
        if connection:
            cursor.close()
            connection.close()
