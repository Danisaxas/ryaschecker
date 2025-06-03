from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import mx as botones_mx
from classBot.MongoDB import MondB

@AstroButton("^mx$")
async def handle_es_mx_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "es_mx"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇲🇽]

¡Éxito! ¡Ahora tu idioma seleccionado es [Español México]!""",
            reply_markup=botones_mx['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
    finally:
        db._client.close()