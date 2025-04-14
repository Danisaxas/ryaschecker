from _date import *
from pyrogram import Client, types
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.BoutnAll import es as botones_es
from Source_pack.BoutnAll import en as botones_en
from classBot.MongoDB import MondB

@AstroButton("^lenguaje$")
async def handle_lenguaje_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username or "Usuario"
        user_data = MondB(idchat=user_id).queryUser()
        lang = user_data.get("lang", "es") if user_data else "es"
        if lang == "es":
            text_dict = text_es
            botones_dict = botones_es
            idioma_actual = "🇪🇸"
        elif lang == "en":
            text_dict = text_en
            botones_dict = botones_en
            idioma_actual = "🇺🇸"
        else:
            text_dict = text_es
            botones_dict = botones_es
            idioma_actual = "🇪🇸"
        await callback_query.message.edit_text(
            text=text_dict["lang_message"].format(username=username, idioma_actual=idioma_actual),
            reply_markup=botones_dict["lang"]
        )
    except Exception as e:
        print(f"Error en handle_lenguaje_button: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
