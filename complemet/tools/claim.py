from _date import *
from pyrogram.client import Client
from pyrogram import types
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

@Astro("claim")
async def redeem_key(client: Client, message: types.Message):
    user_id = message.from_user.id
    user_lang = message.from_user.language_code or 'es'
    user_lang = 'en' if user_lang.startswith('en') else 'es'

    lang_data = load_language_data(user_lang)
    if not lang_data:
        lang_data = load_language_data("es")

    args = message.text.split()
    if len(args) != 2:
        await message.reply_text(
            lang_data['claim_usage'],
            reply_to_message_id=message.id
        )
        return

    key_input = args[1]

    db = MondB()
    key_collection = db._db['key']
    user_collection = db._db['user']

    key_doc = key_collection.find_one({"key": key_input})

    if not key_doc:
        await message.reply_text(
            lang_data['claim_invalid_key'],
            reply_to_message_id=message.id
        )
        return

    status = key_doc.get("status", "off").lower()
    if status != "on":
        await message.reply_text(
            lang_data['claim_key_used'],
            reply_to_message_id=message.id
        )
        return

    dias = key_doc.get("dias", 0)

    user_doc = user_collection.find_one({"_id": user_id})
    if user_doc:
        current_dias = user_doc.get("dias", 0)
        total_dias = current_dias + dias
    else:
        total_dias = dias

    user_collection.update_one(
        {"_id": user_id},
        {
            "$set": {
                "dias": total_dias,
                "key": key_input
            }
        },
        upsert=True
    )

    key_collection.update_one(
        {"_id": key_doc["_id"]},
        {"$set": {"status": "off", "expiracion": None}}
    )

    await message.reply_text(
        lang_data['redeem_success'].format(dias=total_dias),
        reply_to_message_id=message.id
    )