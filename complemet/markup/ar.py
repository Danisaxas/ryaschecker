# ar.py
from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import ar as botones_ar
from classBot.MongoDB import MondB

@AstroButton("^ar$")
async def handle_ar_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "ar"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇸🇦]

نجاح! لغتك المختارة الآن هي [العربية]!""",
            reply_markup=botones_ar['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"حدث خطأ: {e}", reply_markup=None)
    finally:
        db._client.close()