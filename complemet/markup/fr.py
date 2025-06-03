from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import fr as botones_fr
from classBot.MongoDB import MondB

@AstroButton("^fr$")
async def handle_fr_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "fr"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇫🇷] 

Succès! Votre langue sélectionnée est maintenant [Français]!""",
            reply_markup=botones_fr['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Une erreur est survenue: {e}", reply_markup=None)
    finally:
        db._client.close()