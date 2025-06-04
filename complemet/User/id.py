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

@Astro('id')
async def obtener_id(client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username or "No username"

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

    status = user.get("status", "").lower()
    if status == 'ban':
        await message.reply_text(
            lang_data['block_message'],
            reply_to_message_id=message.id
        )
        return

    await message.reply_text(
        lang_data['idtext'].format(
            user_id=user_id,
            chat_id=chat_id,
            username=username
        ),
        reply_to_message_id=message.id
    )