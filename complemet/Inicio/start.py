from _date import *
import pytz
from datetime import datetime
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import pt as text_pt
from Source_pack.TextAll import ru as text_ru
from Source_pack.TextAll import zh as text_zh
from Source_pack.TextAll import ko as text_ko
from Source_pack.BoutnAll import es as btn_es
from Source_pack.BoutnAll import en as btn_en
from Source_pack.BoutnAll import pt as btn_pt
from Source_pack.BoutnAll import ru as btn_ru
from Source_pack.BoutnAll import zh as btn_zh
from Source_pack.BoutnAll import ko as btn_ko

@Astro("start")
async def start(client: Client, message: types.Message):
    user_id = message.from_user.id
    try:
        username = message.from_user.username or "Usuario"
        full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
        user_lang = message.from_user.language_code or 'es'
        user_lang = user_lang.lower()

        valid_langs = {"es", "en", "pt", "ru", "zh", "ko"}
        if not any(user_lang.startswith(lang) for lang in valid_langs):
            user_lang = "es"
        else:
            # Normalize to the valid lang code
            for lang in valid_langs:
                if user_lang.startswith(lang):
                    user_lang = lang
                    break

        user = MondB(idchat=user_id).queryUser()
        if not user:
            text_dict = {
                "es": text_es,
                "en": text_en,
                "pt": text_pt,
                "ru": text_ru,
                "zh": text_zh,
                "ko": text_ko,
            }[user_lang]
            await message.reply_text(text_dict['register_not'], reply_to_message_id=message.id)
            return

        lang = user.get("lang", "es").lower()
        status = user.get("status", "")

        text_dicts = {
            "es": text_es,
            "en": text_en,
            "pt": text_pt,
            "ru": text_ru,
            "zh": text_zh,
            "ko": text_ko,
        }
        botones_dicts = {
            "es": btn_es,
            "en": btn_en,
            "pt": btn_pt,
            "ru": btn_ru,
            "zh": btn_zh,
            "ko": btn_ko,
        }

        if lang not in valid_langs:
            lang = "es"

        text_dict = text_dicts[lang]
        botones_dict = botones_dicts[lang]

        if status == "Baneado":
            text_block = {
                "es": text_es,
                "en": text_en,
                "pt": text_pt,
                "ru": text_ru,
                "zh": text_zh,
                "ko": text_ko,
            }[lang]
            await message.reply_text(text_block['block_message'].format(user_id=user_id), reply_to_message_id=message.id)
            return

        flags = {
            "es": "🇪🇸",
            "en": "🇺🇸",
            "pt": "🇧🇷",
            "ru": "🇷🇺",
            "zh": "🇨🇳",
            "ko": "🇰🇷",
        }
        idioma_actual = flags.get(lang, "🇪🇸")

        caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")

        response = text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=caracas_time)
        await message.reply_text(response, reply_to_message_id=message.id, reply_markup=botones_dict['mainstart'])
    except Exception as e:
        print(f"Error en start: {e}")
