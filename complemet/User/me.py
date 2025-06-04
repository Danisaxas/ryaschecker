from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import Message
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro('me')
async def me_command(client, message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"

    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    if not user:
        await message.reply_text(
            lang_data['register_not'],
            reply_to_message_id=message.id
        )
        return

    rango = user.get("plan")
    creditos = user.get("credits")
    antispam = user.get("antispam")
    expiration = user.get("expiracion")
    status = user.get("status", "")
    ban_status = "Sí" if status.lower() == "baneado" else "No"

    if status.lower() == "baneado":
        await message.reply_text(
            lang_data['block_message'].format(user_id=user_id),
            reply_to_message_id=message.id
        )
        return

    metext = lang_data.get('metext', "")
    formatted_text = metext.format(
        username=username,
        user_id=user_id,
        rango=rango,
        creditos=creditos,
        antispam=antispam,
        expiration=expiration,
        ban=ban_status
    )

    await message.reply_text(
        formatted_text,
        reply_to_message_id=message.id
    )