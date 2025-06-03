from _date import *
from Source_pack.BoutnAll import ru as botones_ru
from classBot.MongoDB import MondB

@AstroButton("^ru$")
async def handle_ru_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "ru"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇷🇺]

Успех! Теперь выбранный вами язык — [Русский]!""",
            reply_markup=botones_ru['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Произошла ошибка: {e}", reply_markup=types.InlineKeyboardMarkup())
    finally:
        db._client.close()
