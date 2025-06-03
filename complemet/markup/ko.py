from _date import *
from Source_pack.BoutnAll import ko as botones_ko
from classBot.MongoDB import MondB

@AstroButton("^ko$")
async def handle_ko_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "ko"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇰🇷]

성공했습니다! 이제 선택한 언어는 [한국어]입니다!""",
            reply_markup=botones_ko['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"오류가 발생했습니다: {e}")
    finally:
        db._client.close()
