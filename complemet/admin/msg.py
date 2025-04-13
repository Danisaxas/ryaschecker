from configs.def_main import *
from pyrogram import Client, types

@ryas("msg")
async def send_message(client: Client, message: types.Message):
    """
    Permite a los administradores enviar mensajes a usuarios específicos o a todos los usuarios,
    teniendo en cuenta el idioma del usuario.
    """
    user_id = message.from_user.id
    connection = None
    try:
        connection, cursor = connect_db()

        cursor.execute("SELECT privilegio, lang FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()

        if not result or result[0] < 3:
            # Cargar el idioma del admin
            admin_lang = result[1] if result else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return

        args = message.text.split(" ", 2)

        if len(args) < 2:
            admin_lang = result[1] if result else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['msgformat'], reply_to_message_id=message.id)
            return

        msg_to_forward = None
        msg_text = None

        if message.reply_to_message:
            msg_to_forward = message.reply_to_message
        else:
            msg_text = args[1] if len(args) == 2 else args[2]

        # Comprobamos si se especifica un ID
        if args[1].startswith("-") or args[1].isdigit():
            target_id = int(args[1])
            cursor.execute("SELECT user_id, lang FROM users WHERE user_id = %s", (target_id,))
            target_user = cursor.fetchone()
            if target_user:
                target_lang = target_user[1]
                if target_lang == 'es':
                    from ryas_templates.chattext import es as text_dict
                else:
                    from ryas_templates.chattext import en as text_dict
                if msg_to_forward:
                    await client.forward_messages(target_id, message.chat.id, msg_to_forward.id)
                else:
                    await client.send_message(target_id, msg_text)

        # Si se usa "all", enviar a todos los usuarios
        elif args[1].lower() == "all":
            cursor.execute("SELECT user_id, lang FROM users")
            users = cursor.fetchall()
            for user in users:
                target_lang = user[1]
                if target_lang == 'es':
                    from ryas_templates.chattext import es as text_dict
                else:
                    from ryas_templates.chattext import en as text_dict
                if msg_to_forward:
                    await client.forward_messages(user[0], message.chat.id, msg_to_forward.id)
                else:
                    await client.send_message(user[0], msg_text)

    except Exception as e:
        print(f"Error en send_message: {e}")
        await message.reply_text(
            "Ocurrió un error al enviar el mensaje.",
            reply_to_message_id=message.id
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
