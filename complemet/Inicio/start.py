from _date import *
import os
import json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_keyboard(buttons_data):
    keyboard = []
    for row in buttons_data:
        keyboard_row = []
        for button in row:
            text = button.get("text", "Botón")
            callback_data = button.get("callback_data")
            url = button.get("url")
            if callback_data:
                kb_button = InlineKeyboardButton(text=text, callback_data=callback_data)
            elif url:
                kb_button = InlineKeyboardButton(text=text, url=url)
            else:
                kb_button = InlineKeyboardButton(text=text, callback_data="none")
            keyboard_row.append(kb_button)
        keyboard.append(keyboard_row)
    return InlineKeyboardMarkup(keyboard)

@Astro("start")
async def start_command(client, message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()
    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es") or {}

    startx_template = lang_data.get("startx")
    if not startx_template or not isinstance(startx_template, str):
        startx_template = "⚠️ No hay mensaje de bienvenida definido."

    mainstart_buttons_data = lang_data.get("mainstart", [])
    reply_markup = build_keyboard(mainstart_buttons_data)

    caracas_time_str = get_capital_time(lang)

    try:
        startx = startx_template.format(
            caracas_time=caracas_time_str,
            idioma_actual=lang.upper(),
            username=message.from_user.username or message.from_user.first_name or "Usuario"
        )
    except Exception as e:
        startx = f"⚠️ Error al formatear el mensaje: {e}"

    await message.reply_text(
        startx,
        reply_markup=reply_markup
    )