from _date import *
from Source_pack.BoutnAll import zh as botones_zh
from classBot.MongoDB import MondB

@AstroButton("^zh$")
async def handle_zh_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "zh"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇨🇳]

成功！您现在选择的语言是 [中文]！""",
            reply_markup=botones_zh['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"发生错误: {e}")
    finally:
        db._client.close()
