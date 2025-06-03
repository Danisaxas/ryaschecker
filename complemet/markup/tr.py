# tr.py
from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import tr as botones_tr
from classBot.MongoDB import MondB

@AstroButton("^tr$")
async def handle_tr_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "tr"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇹🇷]

Başarılı! Seçilen diliniz artık [Türkçe]!""",
            reply_markup=botones_tr['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Bir hata oluştu: {e}", reply_markup=None)
    finally:
        db._client.close()