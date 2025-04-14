from _date import *
from pyrogram import Client, types
from Source_pack.BoutnAll import es as botones_es
from classBot.MongoDB import MondB

@AstroButton("^es$")
async def handle_es_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        user = db.queryUser()
        if user:
            db.updateUser({"lang": "es"})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇪🇸] 

Exito! Ahora su idioma seleccionado es [Español]!""",
            reply_markup=botones_es['back_lang']
        )
    except Exception as e:
        print(f"Error en handle_es_button: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
