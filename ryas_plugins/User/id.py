# ryas_plugins/id.py
from configs.def_main import *
from pyrogram import Client, types

@ryas('id')
async def obtener_id(client: Client, message: types.Message):
    """
    Obtiene y muestra información de ID del usuario y chat, en el idioma del usuario.
    """
    connection = None  # Inicializar connection a None
    try:
        user_id = message.from_user.id
        chat_id = message.chat.id
        username = message.from_user.username if message.from_user.username else "No username"
        reply_msg_id = message.reply_to_message.message_id if message.reply_to_message else message.id

        # Obtener el idioma del usuario desde la base de datos
        connection, cursor = connect_db()
        cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,)) # Obtener lang y ban
        result = cursor.fetchone()
        lang = result[0] if result else 'es'  # Default to 'es' if not found
        ban_status = result[1] if result else 'No' #obtener el estado de baneo
        razon = result[2] if result else ""

        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict  # por defecto español
        
        if ban_status == 'Yes': #verificar si el usuario esta baneado
            await message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=reply_msg_id
            )
            return

        # Enviar el mensaje en el idioma correcto
        await message.reply_text(
            text_dict['idtext'].format(user_id=user_id, chat_id=chat_id, username=username),
            reply_to_message_id=reply_msg_id
        )

    except Exception as e:
        print(f"Error en obtener_id: {e}")
        await message.reply_text(
            "Ocurrió un error al obtener la información.",
            reply_to_message_id=reply_msg_id
        )
    finally:
        if connection:
            cursor.close()
            connection.close()
