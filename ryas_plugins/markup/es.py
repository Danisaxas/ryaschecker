from configs.def_main import *
from pyrogram import Client, types
from ryas_templates.botones import es as botones_dict

@ryasbt("^es$")
async def handle_es_button(client: Client, callback_query: types.CallbackQuery):
    """
    Actualiza el idioma del usuario a español ("es") en la base de datos y muestra un mensaje de confirmación.
    """
    connection = None
    try:
        # Conecta a la base de datos
        connection, cursor = connect_db()

        # Verifica el idioma actual del usuario
        cursor.execute("SELECT lang FROM users WHERE user_id = %s", (callback_query.from_user.id,))
        result = cursor.fetchone()
        current_lang = result[0] if result else 'es'

        if current_lang == 'es':
            await callback_query.message.edit_text(
                "El idioma ya está configurado en Español 🇪🇸",
                reply_markup=botones_dict['back']
            )
        else:
            # Actualiza el idioma del usuario en la tabla 'users'
            update_query = "UPDATE users SET lang = 'es' WHERE user_id = %s"
            cursor.execute(update_query, (callback_query.from_user.id,))
            connection.commit()

            # Responde al usuario con un mensaje de confirmación y el teclado 'back'
            await callback_query.message.edit_text(
                "Se ha puesto el idioma Español 🇪🇸",
                reply_markup=botones_dict['back']  # Usa el teclado del idioma correspondiente
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
