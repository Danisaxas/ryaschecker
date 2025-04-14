from _date import *
from classBot.MongoDB import MondB
from pyrogram import Client, types

@Astro('id')
async def obtener_id(client: Client, message: types.Message):
    try:
        user_id = message.from_user.id
        chat_id = message.chat.id
        username = message.from_user.username or "No username"
        first_name = message.from_user.first_name or ""
        last_name = message.from_user.last_name or ""
        full_name = f"{first_name} {last_name}".strip()
        reply_msg_id = message.reply_to_message.message_id if message.reply_to_message else None
        db = MondB(id=user_id, username=username, name=full_name, idchat=user_id)
        user_data = db.queryUser()
        if not user_data:
            db.savedbuser()
            user_data = db.queryUser()
        lang = user_data.get("lang", "es")
        plan = user_data.get("plan", "Free User")
        status = user_data.get("status", "Libre")
        if lang == 'es':
            from Source_pack.TextAll import es as text_dict
        elif lang == 'en':
            from Source_pack.TextAll import en as text_dict
        else:
            from Source_pack.TextAll import es as text_dict
        if status.lower() == 'ban' or user_data.get("status", "").lower() == "ban":
            await message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=user_data.get("razon", "No especificada")),
                reply_to_message_id=reply_msg_id
            )
            return
        await message.reply_text(
            text_dict['idtext'].format(user_id=user_id, chat_id=chat_id),
            reply_to_message_id=reply_msg_id
        )
    except Exception as e:
        print(f"Error en obtener_id: {e}")
        await message.reply_text(
            "Ocurrió un error al obtener la información.",
            reply_to_message_id=reply_msg_id
        )