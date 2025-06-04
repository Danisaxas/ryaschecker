from _date import *
from classBot.MongoDB import MondB
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@AstroButton("^home$")
async def handle_home(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    startx_template = lang_data.get("startx", "")
    message = startx_template.format(
        caracas_time=caracas_time,
        idioma_actual=lang,
        username=user.username or user.first_name
    )

    await callback_query.message.edit_text(message)
    await callback_query.answer()