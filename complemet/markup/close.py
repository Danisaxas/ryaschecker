from _date import *
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
from classBot.MongoDB import MondB

@AstroButton("^close$")
async def close_callback(client, callback_query):
    user_id = callback_query.from_user.id
    try:
        user_data = MondB(idchat=user_id).queryUser()
        lang = (user_data.get("lang") if user_data else "es") or "es"
        lang = lang.lower()

        valid_langs = {
            "es", "es_mx", "en", "pt", "ru", "zh", "ko",
            "fr", "de", "tr", "ja", "ar", "it"
        }
        if lang not in valid_langs:
            lang = "es"

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

        text_dict = text_dicts[lang]

        await callback_query.message.edit_text(text_dict["close_text"])
    except Exception as e:
        print(f"Error en close_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}")
