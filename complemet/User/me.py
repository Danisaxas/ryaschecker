from _date import *
from classBot.MongoDB import MondB
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from pyrogram.types import Message

@Astro('me')
async def me_command(client, message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"
    user = MondB(idchat=user_id).queryUser()
    if not user:
        lang = "es"
        text_dict = text_es if lang == "es" else text_en
        await message.reply_text(text_dict['register_not'], reply_to_message_id=message.id)
        return
    rango = user.get("plan")
    creditos = user.get("credits")
    antispam = user.get("antispam")
    expiration = user.get("since")
    status = user.get("status")
    lang = user.get("lang")
    if status == "Baneado":
        text_dict = text_es if lang == "es" else text_en
        await message.reply_text(text_dict['block_message'].format(user_id=user_id), reply_to_message_id=message.id)
        return
    text_dict = text_es if lang == "es" else text_en
    formatted_text = text_dict['metext'].format(
        username=username,
        user_id=user_id,
        rango=rango,
        creditos=creditos,
        antispam=antispam,
        expiration=expiration,
        ban="Sí" if status == "Baneado" else "No"
    )
    await message.reply_text(formatted_text, reply_to_message_id=message.id)
