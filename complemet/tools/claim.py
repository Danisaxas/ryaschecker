from _date import *
from pyrogram.client import Client
from pyrogram import types
from classBot.MongoDB import MondB
import json
import os

@Astro("claim")
async def redeem_key(client: Client, message: types.Message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get('lang') if user_data else 'es') or 'es'
    lang = lang.lower()

    data, buttons_data = load_language_file(user_id)

    if not data:
        data, buttons_data = load_language_file("es")

    args = message.text.split()
    if len(args) != 2:
        await message.reply_text(
            data['claim_usage'],
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
            data['claim_invalid_key'],
            reply_to_message_id=message.id
        )
        return

    status = key_doc.get("status", "off").lower()
    if status != "on":
        await message.reply_text(
            data['claim_key_used'],
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
        data['redeem_success'].format(dias=total_dias),
        reply_to_message_id=message.id
    )
