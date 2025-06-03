from _date import *
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import pt as text_pt
from Source_pack.TextAll import ru as text_ru
from Source_pack.TextAll import zh as text_zh
from Source_pack.TextAll import ko as text_ko
from classBot.MongoDB import MondB

@AstroButton("^close$")
async def close_callback(client: Client, callback_query: types.CallbackQuery):
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

        text_dict = text_dicts[lang]

        await callback_query.message.edit_text(text_dict["close_text"])
    except Exception as e:
        print(f"Error en close_callback: {e}")
        await callback_query.message.edit_text(f"Ocurrió un error: {e}")
