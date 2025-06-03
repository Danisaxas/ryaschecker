from _date import *
import pytz
from datetime import datetime
from classBot.MongoDB import MondB
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
    es as btn_es,
    es_mx as btn_es_mx,
    en as btn_en,
    pt as btn_pt,
    ru as btn_ru,
    zh as btn_zh,
    ko as btn_ko,
    fr as btn_fr,
    de as btn_de,
    tr as btn_tr,
    ja as btn_ja,
    ar as btn_ar,
    it as btn_it,
)
from pyrogram import Client, types

@Astro("start")
async def start(client: Client, message: types.Message):
    user_id = message.from_user.id
    try:
        username = message.from_user.username or "Usuario"
        user_lang = (message.from_user.language_code or 'es').lower()
        valid_langs = {
            "es", "es_mx", "en", "pt", "ru", "zh", "ko",
            "fr", "de", "tr", "ja", "ar", "it"
        }
        user_lang = next((lang for lang in valid_langs if user_lang.startswith(lang)), "es")

        user = MondB(idchat=user_id).queryUser()
        if not user:
            text_dict = {
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
            }[user_lang]
            await message.reply_text(text_dict['register_not'], reply_to_message_id=message.id)
            return

        lang = user.get("lang", "es").lower()
        if lang not in valid_langs:
            lang = "es"
        status = user.get("status", "")

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
            "es": btn_es,
            "es_mx": btn_es_mx,
            "en": btn_en,
            "pt": btn_pt,
            "ru": btn_ru,
            "zh": btn_zh,
            "ko": btn_ko,
            "fr": btn_fr,
            "de": btn_de,
            "tr": btn_tr,
            "ja": btn_ja,
            "ar": btn_ar,
            "it": btn_it,
        }

        text_dict = text_dicts[lang]
        botones_dict = botones_dicts[lang]

        if status == "Baneado":
            await message.reply_text(text_dict['block_message'].format(user_id=user_id), reply_to_message_id=message.id)
            return

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
        idioma_actual = flags.get(lang, "🇪🇸")

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
        tz_name, city_country = timezones.get(lang, ("America/Caracas", "Caracas, Venezuela"))
        now = datetime.now(pytz.timezone(tz_name))
        formatted_time = now.strftime(f"%Y-%m-%d {city_country} %I:%M %p")

        response = text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=formatted_time)
        await message.reply_text(response, reply_to_message_id=message.id, reply_markup=botones_dict['mainstart'])
    except Exception as e:
        print(f"Error en start: {e}")