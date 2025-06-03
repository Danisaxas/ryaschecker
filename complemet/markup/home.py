from _date import *
import pytz
from datetime import datetime
from Source_pack.TextAll import (
    es as text_es,
    es_mx as text_es_mx,
    en as text_en,
    pt as text_pt,
    ru as text_ru,
    zh as text_zh,
    ko as text_ko,
    fr as text_fr,
    de as text_de,
    tr as text_tr,
    ja as text_ja,
    ar as text_ar,
    it as text_it,
)
from Source_pack.BoutnAll import (
    es as botones_es,
    es_mx as botones_es_mx,
    en as botones_en,
    pt as botones_pt,
    ru as botones_ru,
    zh as botones_zh,
    ko as botones_ko,
    fr as botones_fr,
    de as botones_de,
    tr as botones_tr,
    ja as botones_ja,
    ar as botones_ar,
    it as botones_it,
)
from classBot.MongoDB import MondB

@AstroButton("^home$")
async def home_callback(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        user_data = MondB(idchat=user_id).queryUser()
        lang = (user_data.get("lang") if user_data else "es") or "es"
        lang = lang.lower()
        valid_langs = {
            "es", "es_mx", "en", "pt", "ru", "zh", "ko",
            "fr", "de", "tr", "ja", "ar", "it"
        }
        if lang not in valid_langs:
            lang = "es"

        flags = {
            "es": "🇪🇸",
            "es_mx": "🇲🇽",
            "en": "🇺🇸",
            "pt": "🇧🇷",
            "ru": "🇷🇺",
            "zh": "🇨🇳",
            "ko": "🇰🇷",
            "fr": "🇫🇷",
            "de": "🇩🇪",
            "tr": "🇹🇷",
            "ja": "🇯🇵",
            "ar": "🇸🇦",
            "it": "🇮🇹",
        }

        timezones = {
            "es": ("Europe/Madrid", "Madrid, Spain"),
            "es_mx": ("America/Mexico_City", "Mexico City, Mexico"),
            "en": ("America/New_York", "Washington DC, United States"),
            "pt": ("America/Sao_Paulo", "São Paulo, Brazil"),
            "ru": ("Europe/Moscow", "Moscow, Russia"),
            "zh": ("Asia/Shanghai", "Beijing, China"),
            "ko": ("Asia/Seoul", "Seoul, South Korea"),
            "fr": ("Europe/Paris", "Paris, France"),
            "de": ("Europe/Berlin", "Berlin, Germany"),
            "tr": ("Europe/Istanbul", "Istanbul, Turkey"),
            "ja": ("Asia/Tokyo", "Tokyo, Japan"),
            "ar": ("Asia/Riyadh", "Riyadh, Saudi Arabia"),
            "it": ("Europe/Rome", "Rome, Italy"),
        }

        text_dicts = {
            "es": text_es,
            "es_mx": text_es_mx,
            "en": text_en,
            "pt": text_pt,
            "ru": text_ru,
            "zh": text_zh,
            "ko": text_ko,
            "fr": text_fr,
            "de": text_de,
            "tr": text_tr,
            "ja": text_ja,
            "ar": text_ar,
            "it": text_it,
        }

        botones_dicts = {
            "es": botones_es,
            "es_mx": botones_es_mx,
            "en": botones_en,
            "pt": botones_pt,
            "ru": botones_ru,
            "zh": botones_zh,
            "ko": botones_ko,
            "fr": botones_fr,
            "de": botones_de,
            "tr": botones_tr,
            "ja": botones_ja,
            "ar": botones_ar,
            "it": botones_it,
        }

        idioma_actual = flags[lang]
        tz_name, city_country = timezones.get(lang, ("America/Caracas", "Caracas, Venezuela"))

        text_key = lang
        botones_key = "mx" if lang == "es_mx" else lang

        text_dict = text_dicts[text_key]
        botones_dict = botones_dicts[botones_key]

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
