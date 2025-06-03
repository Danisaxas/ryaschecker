from _date import *
import pytz
from datetime import datetime
from Source_pack.TextAll import es as text_es, en as text_en, pt as text_pt, ru as text_ru, zh as text_zh, ko as text_ko
from Source_pack.BoutnAll import es as botones_es, en as botones_en, pt as botones_pt, ru as botones_ru, zh as botones_zh, ko as botones_ko
from classBot.MongoDB import MondB

@AstroButton("^home$")
async def home_callback(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        user_data = MondB(idchat=user_id).queryUser()
        lang = (user_data.get("lang") if user_data else "es") or "es"
        lang = lang.lower()
        if lang not in {"es","en","pt","ru","zh","ko"}:
            lang = "es"
        flags = {"es":"🇪🇸","en":"🇺🇸","pt":"🇧🇷","ru":"🇷🇺","zh":"🇨🇳","ko":"🇰🇷"}
        timezones = {"es":"Europe/Madrid","en":"America/New_York","pt":"America/Sao_Paulo","ru":"Europe/Moscow","zh":"Asia/Shanghai","ko":"Asia/Seoul"}
        idioma_actual = flags[lang]
        timezone_str = timezones[lang]
        text_dict = {"es":text_es,"en":text_en,"pt":text_pt,"ru":text_ru,"zh":text_zh,"ko":text_ko}[lang]
        botones_dict = {"es":botones_es,"en":botones_en,"pt":botones_pt,"ru":botones_ru,"zh":botones_zh,"ko":botones_ko}[lang]
        username = callback_query.from_user.username or "Usuario"
        local_time = datetime.now(pytz.timezone(timezone_str)).strftime("%Y-%m-%d %Z, %I:%M %p")
        await callback_query.message.edit_text(
            text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=local_time),
            reply_markup=botones_dict['mainstart']
        )
    except Exception as e:
        print(f"Error en home_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}")