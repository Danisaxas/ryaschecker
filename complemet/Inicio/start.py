from _date import *
import os
import json
from pyrogram.types import InlineKeyboardMarkup

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("start")
async def start_command(client, message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()

    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es") or {}

    startx_template = lang_data.get("startx", "")
    mainstart_buttons = lang_data.get("mainstart", [])

    await message.reply_text(
        startx_template.format(
            caracas_time=caracas_time(),
            idioma_actual=lang,
            username=message.from_user.username or message.from_user.first_name or "Usuario"
        ),
        reply_markup=InlineKeyboardMarkup(mainstart_buttons)
    )