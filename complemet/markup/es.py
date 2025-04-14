from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import es as botones_es
from classBot.MongoDB import MondB

@AstroButton("^es$")
async def handle_es_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        mdb = MondB(idchat=user_id)
        _database = mdb._client['bot']
        _collection = _database['user']
        _collection.update_one({"id": user_id}, {"$set": {"lang": "es"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇪🇸] 

Exito! Ahora su idioma seleccionado es [Español]!""",
            reply_markup=botones_es['back_lang']
        )
    except Exception as e:
        print(f"Error en handle_es_button: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
    finally:
        mdb._client.close()
