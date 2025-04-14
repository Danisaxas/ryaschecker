from _date import *
from pyrogram import Client, types
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from classBot.MongoDB import MondB

@AstroButton("^close$")
async def close_callback(client: Client, callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    try:
        user_data = MondB(idchat=user_id).queryUser()
        lang = user_data.get("lang", "es") if user_data else "es"
        if lang == "es":
            text_dict = text_es
        elif lang == "en":
            text_dict = text_en
        else:
            text_dict = text_es
        await callback_query.message.edit_text(text_dict["close_text"])
    except Exception as e:
        print(f"Error en close_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
