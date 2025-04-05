from configs.def_main import *
from pyrogram import Client, types
import mysql.connector
from datetime import datetime

@ryas("unban")
async def unban_user(client: Client, message: types.Message):
    """
    Desbanea a un usuario del bot, eliminando la razón de baneo de la base de datos.
    Solo los usuarios con privilegio mayor a 2 pueden usar este comando.
    """
    connection = None
    try:
        admin_id = message.from_user.id
        admin_username = message.from_user.username or "Usuario"

        connection, cursor = connect_db()

        # Verificar los privilegios del administrador
        cursor.execute("SELECT privilegio, lang FROM users WHERE user_id = %s", (admin_id,))
        admin_data = cursor.fetchone()

        if not admin_data or admin_data[0] < 3:
            # Cargar el idioma del administrador para el mensaje de error
            admin_lang = admin_data[1] if admin_data else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return

        # Obtener los argumentos del comando
        args = message.text.split()  # Dividir el mensaje por espacios
        if len(args) != 2:
            admin_lang = admin_data[1] if admin_data else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['unban_usage'], reply_to_message_id=message.id)
            return

        target_user_id = args[1]

        # Verificar si el ID es un entero válido
        try:
            target_user_id = int(target_user_id)
        except ValueError:
            admin_lang = admin_data[1] if admin_data else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['unban_validation'], reply_to_message_id=message.id)
            return

        # Actualizar el estado del usuario en la base de datos
        cursor.execute("UPDATE users SET ban = 'No', razon = NULL WHERE user_id = %s", (target_user_id,))
        connection.commit()

        # Obtener el nombre de usuario del usuario desbaneado
        cursor.execute("SELECT username, lang FROM users WHERE user_id = %s", (target_user_id,))
        target_user_data = cursor.fetchone()
        target_username = target_user_data[0] if target_user_data else "Desconocido"
        target_lang = target_user_data[1] if target_user_data else 'es'

        # Cargar el idioma para el mensaje de confirmación
        if target_lang == 'es':
            from ryas_templates.chattext import es as text_dict
        else:
            from ryas_templates.chattext import en as text_dict
            
        unban_message = text_dict['unban_message'].format(
            username=target_username,
            target_user_id=target_user_id,
            admin_username=admin_username,
            admin_id=admin_id,
            fecha=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        await message.reply_text(unban_message, reply_to_message_id=message.id)

    except mysql.connector.Error as e:
        print(f"Error al desbanear usuario: {e}")
        await message.reply_text(f"Ocurrió un error al desbanear al usuario: {e}", reply_to_message_id=message.id)
    except Exception as e:
        print(f"Error inesperado: {e}")
        await message.reply_text(f"Ocurrió un error inesperado: {e}", reply_to_message_id=message.id)
    finally:
        if connection:
            cursor.close()
            connection.close()
