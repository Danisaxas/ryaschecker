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
        valid_langs = {"es","en","pt","ru","zh","ko"}
        if lang not in valid_langs:
            lang = "es"
        flags = {"es":"🇪🇸","en":"🇺🇸","pt":"🇧🇷","ru":"🇷🇺","zh":"🇨🇳","ko":"🇰🇷"}
        timezones = {
            "es": ("Europe/Madrid", "Madrid, Spain"),
            "en": ("America/New_York", "Washington DC, United States"),
            "pt": ("America/Sao_Paulo", "São Paulo, Brazil"),
            "ru": ("Europe/Moscow", "Moscow, Russia"),
            "zh": ("Asia/Shanghai", "Beijing, China"),
            "ko": ("Asia/Seoul", "Seoul, South Korea"),
        }
        idioma_actual = flags[lang]
        tz_name, city_country = timezones.get(lang, ("America/Caracas", "Caracas, Venezuela"))
        text_dicts = {
            "es": text_es,
            "en": text_en,
            "pt": text_pt,
            "ru": text_ru,
            "zh": text_zh,
            "ko": text_ko,
        }
        botones_dicts = {
            "es": botones_es,
            "en": botones_en,
            "pt": botones_pt,
            "ru": botones_ru,
            "zh": botones_zh,
            "ko": botones_ko,
        }
        text_dict = text_dicts[lang]
        botones_dict = botones_dicts[lang]
        username = callback_query.from_user.username or "Usuario"
        now = datetime.now(pytz.timezone(tz_name))
        local_time = now.strftime(f"%Y-%m-%d {city_country} %I:%M %p")
        await callback_query.message.edit_text(
            text=text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=local_time),
            reply_markup=botones_dict['mainstart']
        )
    except Exception as e:
        print(f"Error en home_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}")