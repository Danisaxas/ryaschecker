from _date import *
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import pt as text_pt
from Source_pack.TextAll import ru as text_ru
from Source_pack.TextAll import zh as text_zh
from Source_pack.TextAll import ko as text_ko
from pyrogram.types import Message

@Astro('me')
async def me_command(client, message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"
    user = MondB(idchat=user_id).queryUser()

    if not user:
        lang = "es"
        text_dict = text_es
        await message.reply_text(text_dict['register_not'], reply_to_message_id=message.id)
        return

    rango = user.get("plan")
    creditos = user.get("credits")
    antispam = user.get("antispam")
    expiration = user.get("expiracion")
    status = user.get("status")
    lang = user.get("lang", "es").lower()

    valid_langs = {"es", "en", "pt", "ru", "zh", "ko"}
    if lang not in valid_langs:
        lang = "es"

    text_dicts = {
        "es": text_es,
        "en": text_en,
        "pt": text_pt,
        "ru": text_ru,
        "zh": text_zh,
        "ko": text_ko,
    }

    text_dict = text_dicts[lang]

    if status == "Baneado":
        block_text = {
            "es": text_es,
            "en": text_en,
            "pt": text_pt,
            "ru": text_ru,
            "zh": text_zh,
            "ko": text_ko,
        }[lang]
        await message.reply_text(block_text['block_message'].format(user_id=user_id), reply_to_message_id=message.id)
        return

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