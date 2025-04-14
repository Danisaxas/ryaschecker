from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import en as botones_en
from classBot.MongoDB import MondB

@AstroButton("^en$")
async def handle_en_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        mdb = MondB(idchat=user_id)
        _database = mdb._client['bot']
        _collection = _database['user']
        _collection.update_one({"id": user_id}, {"$set": {"lang": "en"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇺🇸]

Success! Now your selected language is [English]!""",
            reply_markup=botones_en['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(
            f"An error occurred: {e}",
            reply_markup=None
        )
    finally:
        mdb._client.close()
