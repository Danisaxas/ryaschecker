from _date import *
from Source_pack.TextAll import (
    es as text_es,
    en as text_en,
    pt as text_pt,
    ru as text_ru,
    zh as text_zh,
    ko as text_ko,
    fr as text_fr,
    es_mx as text_mx,
    tr as text_tr,
    ar as text_ar,
    de as text_de,
    ja as text_ja,
    it as text_it,
)
from Source_pack.BoutnAll import (
    es as botones_es,
    en as botones_en,
    pt as botones_pt,
    ru as botones_ru,
    zh as botones_zh,
    ko as botones_ko,
    fr as botones_fr,
    es_mx as botones_es_mx,
    tr as botones_tr,
    ar as botones_ar,
    de as botones_de,
    ja as botones_ja,
    it as botones_it,
)
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardMarkup

@AstroButton("^tools$")
async def tools_callback(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        user_data = MondB(idchat=user_id).queryUser()
        lang = (user_data.get("lang", "es") if user_data else "es").lower()

        valid_langs = {
            "es", "en", "pt", "ru", "zh", "ko",
            "fr", "es_mx", "tr", "ar", "de", "ja", "it"
        }
        if lang not in valid_langs:
            lang = "es"

        text_dicts = {
            "es": text_es,
            "en": text_en,
            "pt": text_pt,
            "ru": text_ru,
            "zh": text_zh,
            "ko": text_ko,
            "fr": text_fr,
            "es_mx": text_es_mx,
            "tr": text_tr,
            "ar": text_ar,
            "de": text_de,
            "ja": text_ja,
            "it": text_it,
        }

        botones_dicts = {
            "es": botones_es,
            "en": botones_en,
            "pt": botones_pt,
            "ru": botones_ru,
            "zh": botones_zh,
            "ko": botones_ko,
            "fr": botones_fr,
            "es_mx": botones_es_mx,
            "tr": botones_tr,
            "ar": botones_ar,
            "de": botones_de,
            "ja": botones_ja,
            "it": botones_it,
        }

        text_dict = text_dicts[lang]
        botones_dict = botones_dicts[lang]

        await callback_query.message.edit_text(
            text_dict["tools"],
            reply_markup=botones_dict["atras"],
        )
    except Exception as e:
        print(f"Error en tools_callback: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=InlineKeyboardMarkup([]),
        )