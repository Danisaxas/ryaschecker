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
        if lang == "es":
            await message.reply_text(text_es['register_not'], reply_to_message_id=message.id)
        else:
            await message.reply_text(text_en['register_not'], reply_to_message_id=message.id)
        return

    rango = user.get("plan")
    creditos = user.get("credits")
    antispam = user.get("antispam")
    expiration = user.get("since")
    ban = "No" if user.get("status") == "Libre" else "Sí"
    lang = user.get("lang")

    text_dict = text_es if lang == "es" else text_en

    formatted_text = text_dict['metext'].format(
        username=username,
        user_id=user_id,
        rango=rango,
        creditos=creditos,
        antispam=antispam,
        expiration=expiration,
        ban=ban
    )

    await message.reply_text(formatted_text, reply_to_message_id=message.id)
