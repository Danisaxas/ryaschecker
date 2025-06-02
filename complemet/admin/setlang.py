from _date import *
from classBot.MongoDB import MondB
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from pyrogram.types import Message

@Astro("setlang")
async def comando_setlang(client, message: Message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()

    lang = user_data.get("lang", "es") if user_data else "es"
    lang = lang.lower()
    lang = 'en' if lang.startswith('en') else 'es'
    text = text_en if lang == "en" else text_es

    if str(user_id) != str(owner):
        await message.reply_text(
            text['setrol_no_permission'],
            reply_to_message_id=message.id
        )
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
