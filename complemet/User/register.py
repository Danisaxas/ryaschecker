from _date import *
from pyrogram import Client, types
from classBot.MongoDB import MondB
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro('register')
async def register_user(client: Client, message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
    lang = message.from_user.language_code or "es"
    lang = 'en' if lang.startswith("en") else "es"

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    try:
        db = MondB(id=user_id, username=username, name=full_name, idchat=user_id)
        if db.queryUser():
            await message.reply_text(
                lang_data['already_registered'].format(user=username),
                reply_to_message_id=message.id
            )
            return

        db.savedbuser()

        registro_msg = lang_data['registerx'].format(username=username, user_id=user_id, lang=lang.upper())
        await message.reply_text(
            registro_msg,
            reply_to_message_id=message.id
        )
    except Exception as e:
        print(f"Error en register_user: {e}")