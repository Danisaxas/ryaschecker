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
)
from Source_pack.BoutnAll import (
    es as botones_es,
    en as botones_en,
    pt as botones_pt,
    ru as botones_ru,
    zh as botones_zh,
    ko as botones_ko,
    fr as botones_fr,
    MX as botones_mx,
    tr as botones_tr,
    ar as botones_ar,
    de as botones_de,
)
from classBot.MongoDB import MondB

@AstroButton("^ryas_cloud$")
async def handle_ryas_cloud_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username or "Usuario"
        user_data = MondB(idchat=user_id).queryUser()
        lang = (user_data.get("lang") if user_data else "es").lower()

        valid_langs = {"es", "en", "pt", "ru", "zh", "ko", "fr", "mx", "tr", "ar", "de"}
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
            "mx": text_mx,
            "tr": text_tr,
            "ar": text_ar,
            "de": text_de,
        }
        botones_dicts = {
            "es": botones_es,
            "en": botones_en,
            "pt": botones_pt,
            "ru": botones_ru,
            "zh": botones_zh,
            "ko": botones_ko,
            "fr": botones_fr,
            "mx": botones_mx,
            "tr": botones_tr,
            "ar": botones_ar,
            "de": botones_de,
        }

        text_dict = text_dicts[lang]
        botones_dict = botones_dicts[lang]

        await callback_query.message.edit_text(
            text=text_dict['ryas_cloud'].format(username=username),
            reply_markup=botones_dict['vryasx']
        )
    except Exception as e:
        print(f"Error en handle_ryas_cloud_button: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=None
        )