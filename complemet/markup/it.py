# it.py
from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import it as botones_it
from classBot.MongoDB import MondB

@AstroButton("^it$")
async def handle_it_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "it"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇮🇹]

Successo! La tua lingua selezionata è ora [Italiano]!""",
            reply_markup=botones_it['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Si è verificato un errore: {e}", reply_markup=None)
    finally:
        db._client.close()