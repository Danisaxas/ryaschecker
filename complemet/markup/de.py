# de.py
from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import de as botones_de
from classBot.MongoDB import MondB

@AstroButton("^de$")
async def handle_de_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "de"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇩🇪]

Erfolg! Ihre ausgewählte Sprache ist jetzt [Deutsch]!""",
            reply_markup=botones_de['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Ein Fehler ist aufgetreten: {e}", reply_markup=None)
    finally:
        db._client.close()