from _date import *
from pyrogram import Client, types
import pytz
from datetime import datetime
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.BoutnAll import es as botones_es
from Source_pack.BoutnAll import en as botones_en
from classBot.MongoDB import MondB

@AstroButton("^home$")
async def home_callback(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
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
        username = callback_query.from_user.username or "Usuario"
        caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")
        await callback_query.message.edit_text(
            text=text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=caracas_time),
            reply_markup=botones_dict['mainstart']
        )
    except Exception as e:
        print(f"Error en home_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}", reply_markup=None)
