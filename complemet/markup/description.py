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

@AstroButton("^description$")
async def description_callback(client: Client, callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    try:
        user_data = MondB(idchat=user_id).queryUser()
        lang = user_data.get("lang", "es") if user_data else "es"
        lang = lang.lower()

        valid_langs = {"es", "en", "pt", "ru", "zh", "ko"}
        if lang not in valid_langs:
            lang = "es"

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

        await callback_query.message.edit_text(
            text_dict["description_text"],
            reply_markup=botones_dict["back"]
        )
    except Exception as e:
        print(f"Error en description_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}")
