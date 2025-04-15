from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import es as botones_es
from classBot.MongoDB import MondB

@AstroButton("^es$")
async def handle_es_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "es"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇪🇸] 

Exito! Ahora su idioma seleccionado es [Español]!""",
            reply_markup=botones_es['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
    finally:
        db._client.close()
