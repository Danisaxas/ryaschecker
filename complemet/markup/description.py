from _date import *
from pyrogram import Client, types
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.BoutnAll import es as botones_es
from Source_pack.BoutnAll import en as botones_en
from classBot.MongoDB import MondB

@AstroButton("^description$")
async def description_callback(client: Client, callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    try:
        user_data = MondB(idchat=user_id).queryUser()
        lang = user_data.get("lang", "es") if user_data else "es"
        if lang == "es":
            text_dict = text_es
            botones_dict = botones_es
        elif lang == "en":
            text_dict = text_en
            botones_dict = botones_en
        else:
            text_dict = text_es
            botones_dict = botones_es
        await callback_query.message.edit_text(
            text_dict["description_text"],
            reply_markup=botones_dict["back"]
        )
    except Exception as e:
        print(f"Error en description_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
