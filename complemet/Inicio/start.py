from _date import *
import json
import os
from classBot.MongoDB import MondB

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("start")
async def start_command(client, message):
    user = message.from_user
    user_id = user.id

    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    startx_template = lang_data.get("startx", "")
    message_text = startx_template.format(
        caracas_time=caracas_time,
        idioma_actual=lang,
        username=user.username or user.first_name
    )

    mainstart_buttons = lang_data.get("mainstart", [])

    await message.reply_text(
        message_text,
        reply_markup={"inline_keyboard": mainstart_buttons}
    )