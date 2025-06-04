from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
import os
from classBot.MongoDB import MondB
from datetime import datetime
import pytz
from _date import *

@Astro("Start")
async def start(client, message):
    user_id = message.chat.id
    username = message.from_user.username or "Usuario"

    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()

    locales_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "locales")
    buttons_path = os.path.join(locales_path, "button_layouts")

    lang_file = os.path.join(locales_path, f"{lang}.json")
    buttons_file = os.path.join(buttons_path, f"{lang}.json")

    # Verificar si el archivo de idioma existe
    if os.path.exists(lang_file):
        with open(lang_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        with open(os.path.join(locales_path, "es.json"), "r", encoding="utf-8") as f:
            data = json.load(f)

    # Verificar si el archivo de botones existe
    if os.path.exists(buttons_file):
        with open(buttons_file, "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    else:
        with open(os.path.join(buttons_path, "es.json"), "r", encoding="utf-8") as f:
            buttons_data = json.load(f)

    start_text = data.get("startx", "¡Bienvenido!")
    
    mainstart_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("mainstart", [])
    ]

    timezone = pytz.timezone("America/Caracas")
    caracas_time = datetime.now(timezone).strftime("%H:%M:%S")

    idioma_actual = f"{LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')} {lang.upper()}"

    message_text = start_text.format(caracas_time=caracas_time, username=username, idioma_actual=idioma_actual)

    if message.reply_to_message:
        reply_to_message_id = message.reply_to_message.message_id
    else:
        reply_to_message_id = None

    await client.send_message(
        chat_id=user_id,
        text=message_text,
        reply_markup=InlineKeyboardMarkup(mainstart_buttons),
        reply_to_message_id=reply_to_message_id
    )