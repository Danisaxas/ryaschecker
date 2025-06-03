# ja.py
from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import ja as botones_ja
from classBot.MongoDB import MondB

@AstroButton("^ja$")
async def handle_ja_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "ja"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇯🇵]

成功！選択した言語は現在 [日本語] です！""",
            reply_markup=botones_ja['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"エラーが発生しました: {e}", reply_markup=None)
    finally:
        db._client.close()