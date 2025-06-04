from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import Message
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

IDIOMAS_VALIDOS = [
    "ar", "mx", "es", "en", "tr", "ru", "pt", "ko", "ch",
    "fr", "de", "vi", "id", "it", "ja"
]

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("setlang")
async def comando_setlang(client, message: Message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()

    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()
    for code in IDIOMAS_VALIDOS:
        if lang.startswith(code):
            lang = code
            break
    else:
        lang = "es"

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    if str(user_id) != str(owner):
        await message.reply_text(
            lang_data['setrol_no_permission'],
            reply_to_message_id=message.id
        )
        return

    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text(
            lang_data['setlang_usage'],
            reply_to_message_id=message.id
        )
        return

    try:
        target_id = int(args[1])
    except ValueError:
        await message.reply_text(
            lang_data['setlang_invalid_id'],
            reply_to_message_id=message.id
        )
        return

    nuevo_idioma = args[2].lower()
    if nuevo_idioma not in IDIOMAS_VALIDOS:
        await message.reply_text(
            lang_data['setlang_invalid_lang'],
            reply_to_message_id=message.id
        )
        return

    db = MondB(idchat=target_id)
    _database = db._client['bot']
    _collection = _database['user']

    target_user = _collection.find_one({"_id": target_id})
    if not target_user:
        await message.reply_text(
            lang_data['setlang_not_found'],
            reply_to_message_id=message.id
        )
        db._client.close()
        return

    _collection.update_one({"_id": target_id}, {"$set": {"lang": nuevo_idioma}})

    await message.reply_text(
        lang_data['setlang_success'].format(id=target_id, idioma=nuevo_idioma),
        reply_to_message_id=message.id
    )
    db._client.close()