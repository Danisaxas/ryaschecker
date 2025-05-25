from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import Message
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es

@Astro('id')
async def obtener_id(client: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username or "No username"
    user = MondB(idchat=user_id).queryUser()
    if not user:
        lang = "es"
        text_dict = text_es if lang == "es" else text_en
        await message.reply_text(text_dict['register_not'], reply_to_message_id=message.id)
        return
    lang = user.get("lang")
    plan = user.get("plan")
    status = user.get("status")
    text_dict = text_es if lang == "es" else text_en
    if status.lower() == 'ban':
        await message.reply_text(
            text_dict['block_message'].format(user_id=user_id, razon=user.get("razon", "No especificada")),
            reply_to_message_id=message.id
        )
        return
    await message.reply_text(
        text_dict['idtext'].format(user_id=user_id, chat_id=chat_id, username=username),
        reply_to_message_id=message.id
    )