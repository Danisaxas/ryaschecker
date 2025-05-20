from _date import *
from pyrogram.client import Client
from pyrogram import types
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from datetime import datetime

@Astro("redeem")
async def redeem_key(client: Client, message: types.Message):
    user_id = message.from_user.id
    user_lang = message.from_user.language_code or 'es'
    user_lang = 'en' if user_lang.startswith('en') else 'es'
    text_dict = text_en if user_lang == 'en' else text_es

    args = message.text.split()
    if len(args) != 2:
        await message.reply_text(
            "<b>Usage: /redeem <YourKey></b>" if user_lang == 'en' else "<b>Uso: /redeem <TuKey></b>",
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
            "<b>Invalid key.</b>" if user_lang == 'en' else "<b>Key inválida.</b>",
            reply_to_message_id=message.id
        )
        return

    status = key_doc.get("status", "off").lower()
    if status != "on":
        await message.reply_text(
            "<b>This key has already been redeemed or is expired.</b>" if user_lang == 'en' else "<b>Esta key ya fue canjeada o está expirada.</b>",
            reply_to_message_id=message.id
        )
        return

    dias = key_doc.get("dias", 0)

    user_collection.update_one(
        {"_id": user_id},
        {
            "$set": {
                "dias": dias,
                "key": key_input
            }
        },
        upsert=True
    )

    key_collection.update_one(
        {"_id": key_doc["_id"]},
        {"$set": {"status": "off", "expiracion": None}}
    )

    msg = text_dict.get('redeem_success', 
            "<b>Key redeemed successfully! You now have {dias} days.</b>" if user_lang == 'en' else
            "<b>Key canjeada con éxito! Ahora tienes {dias} días.</b>"
        ).format(dias=dias)

    await message.reply_text(msg, reply_to_message_id=message.id)
