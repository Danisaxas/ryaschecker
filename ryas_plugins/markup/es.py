# markup/es.py
from configs.def_main import *

@ryasbt("^es$")
async def handle_es_button(client: Client, callback_query: types.CallbackQuery):
    """
    Actualiza el idioma del usuario a español ("es") en la base de datos.
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

        # Responde al usuario
        await callback_query.message.edit_text(
            "Tu idioma ha sido configurado a español.",
            reply_markup=None  # Elimina el teclado anterior
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
