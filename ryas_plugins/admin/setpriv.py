from configs.def_main import *
from pyrogram import Client, types

@ryas("setpriv")
async def set_priv(client: Client, message: types.Message):
    """
    Permite al propietario del bot establecer privilegios de usuario, teniendo en cuenta el idioma del usuario.
    """
    user_id = message.from_user.id
    connection = None
    try:
        connection, cursor = connect_db()

        cursor.execute("SELECT privilegio, lang FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()

        if not result or result[0] != int(OWNER_ID):
            # Cargar el idioma del admin
            admin_lang = result[1] if result else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return

        args = message.text.split(" ")
        if len(args) != 3:
            admin_lang = result[1] if result else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
            else:
                from ryas_templates.chattext import en as text_dict
            await message.reply_text(text_dict['setpriv_usage'], reply_to_message_id=message.id)
            return

        _, target_user_id, privilegio = args
        try:
            target_user_id = int(target_user_id.strip())
            privilegio = int(privilegio.strip())
        except ValueError:
            admin_lang = result[1] if result else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
                await message.reply_text(text_dict['setpriv_value_error'], reply_to_message_id=message.id)
            else:
                from ryas_templates.chattext import en as text_dict
                await message.reply_text(text_dict['setpriv_value_error'], reply_to_message_id=message.id)
            return

        cursor.execute("SELECT rango, lang FROM users WHERE user_id = %s", (target_user_id,))
        target_user = cursor.fetchone()

        if target_user:
            cursor.execute("UPDATE users SET privilegio = %s WHERE user_id = %s", (privilegio, target_user_id))
            connection.commit()
            target_lang = target_user[1]
            if target_lang == 'es':
                from ryas_templates.chattext import es as text_dict
                await message.reply_text(
                    text_dict['setpriv_success'].format(user_id=target_user_id),
                    reply_to_message_id=message.id
                )
            else:
                from ryas_templates.chattext import en as text_dict
                await message.reply_text(
                    text_dict['setpriv_success'].format(user_id=target_user_id),
                    reply_to_message_id=message.id
                )
        else:
            admin_lang = result[1] if result else 'es'
            if admin_lang == 'es':
                from ryas_templates.chattext import es as text_dict
                await message.reply_text(
                    text_dict['setpriv_not_found'],
                    reply_to_message_id=message.id
                )
            else:
                from ryas_templates.chattext import en as text_dict
                await message.reply_text(
                    text_dict['setpriv_not_found'],
                    reply_to_message_id=message.id
                )

    except Exception as e:
        print(f"Error en set_priv: {e}")
        await message.reply_text(
            "Ocurrió un error al procesar el comando setpriv.",
            reply_to_message_id=message.id
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
