import json
import os
from _date import *
from classBot.MongoDB import MondB
from datetime import datetime
import pytz

@Astro("Start")
async def start(client, message):
    user_id = message.chat.id
    username = message.from_user.username or "Usuario"

    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()

    base_path = os.path.dirname(os.path.abspath(__file__))
    locales_path = os.path.abspath(os.path.join(base_path, "..", "..", "locales"))
    
    lang_file = os.path.join(locales_path, f"{lang}.json")
    buttons_file = os.path.join(locales_path, "button_layouts", f"{lang}.json")

    try:
        with open(lang_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        with open(os.path.join(locales_path, "es.json"), "r", encoding="utf-8") as f:
            data = json.load(f)

    try:
        with open(buttons_file, "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    except Exception:
        with open(os.path.join(locales_path, "button_layouts", "es.json"), "r", encoding="utf-8") as f:
            buttons_data = json.load(f)

    start_text = data.get("startx", "¡Bienvenido!")
    mainstart_buttons = buttons_data.get("mainstart", [])

    timezone = pytz.timezone("America/Caracas")
    caracas_time = datetime.now(timezone).strftime("%H:%M:%S")

    # Obtener la bandera correspondiente al idioma
    idioma_actual = f"{LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')} {lang.upper()}"

    message_text = start_text.format(caracas_time=caracas_time, username=username, idioma_actual=idioma_actual)

    await client.send_message(
        chat_id=user_id,
        text=message_text,
        reply_markup=InlineKeyboardMarkup(mainstart_buttons)
    )