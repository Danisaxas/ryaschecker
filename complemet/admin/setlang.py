from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import Message
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es

RANGOS_PERMITIDOS = [4, 5, 6]

@Astro("setlang")
async def comando_setlang(client, message: Message):
    user_id = message.from_user.id
    user = MondB(idchat=user_id).queryUser()

    if not user:
        await message.reply_text(text_es['register_not'], reply_to_message_id=message.id)
        return

    lang = user.get("lang", "es")
    rango = user.get("rango", 0)
    text = text_es if lang == "es" else text_en

    if rango not in RANGOS_PERMITIDOS:
        await message.reply_text(text['not_privilegios'], reply_to_message_id=message.id)
        return

    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text(text['setlang_usage'], reply_to_message_id=message.id)
        return

    try:
        target_id = int(args[1])
    except ValueError:
        await message.reply_text(text['setlang_invalid_id'], reply_to_message_id=message.id)
        return

    nuevo_idioma = args[2].lower()
    if nuevo_idioma not in ["es", "en"]:
        await message.reply_text(text['setlang_invalid_lang'], reply_to_message_id=message.id)
        return

    db = MondB(idchat=target_id)
    _database = db._client['bot']
    _collection = _database['user']

    target_user = _collection.find_one({"_id": target_id})
    if not target_user:
        await message.reply_text(text['setlang_not_found'], reply_to_message_id=message.id)
        db._client.close()
        return

    _collection.update_one({"_id": target_id}, {"$set": {"lang": nuevo_idioma}})
    await message.reply_text(
        text['setlang_success'].format(id=target_id, idioma=nuevo_idioma),
        reply_to_message_id=message.id
    )
    db._client.close()
