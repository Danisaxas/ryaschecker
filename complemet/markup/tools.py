from _date import *
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import pt as text_pt
from Source_pack.TextAll import ru as text_ru
from Source_pack.TextAll import zh as text_zh
from Source_pack.TextAll import ko as text_ko
from Source_pack.BoutnAll import es as botones_es
from Source_pack.BoutnAll import en as botones_en
from Source_pack.BoutnAll import pt as botones_pt
from Source_pack.BoutnAll import ru as botones_ru
from Source_pack.BoutnAll import zh as botones_zh
from Source_pack.BoutnAll import ko as botones_ko
from classBot.MongoDB import MondB

@AstroButton("^tools$")
async def tools_callback(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        user_data = MondB(idchat=user_id).queryUser()
        lang = user_data.get("lang", "es") if user_data else "es"
        lang = lang.lower()
        lang = "en" if lang.startswith("en") else lang
        lang = "pt" if lang.startswith("pt") else lang
        lang = "ru" if lang.startswith("ru") else lang
        lang = "zh" if lang.startswith("zh") else lang
        lang = "ko" if lang.startswith("ko") else lang
        lang = "es" if lang not in ["en", "pt", "ru", "zh", "ko"] else lang

        text_dict = {
            "es": text_es,
            "en": text_en,
            "pt": text_pt,
            "ru": text_ru,
            "zh": text_zh,
            "ko": text_ko
        }[lang]

        botones_dict = {
            "es": botones_es,
            "en": botones_en,
            "pt": botones_pt,
            "ru": botones_ru,
            "zh": botones_zh,
            "ko": botones_ko
        }[lang]

        await callback_query.message.edit_text(
            text_dict['tools'],
            reply_markup=botones_dict['atras']
        )
    except Exception as e:
        print(f"Error en tools_callback: {e}")
        await callback_query.message.edit_text(
            f"Ocurrió un error: {e}",
            reply_markup=InlineKeyboardMarkup([])
        )
