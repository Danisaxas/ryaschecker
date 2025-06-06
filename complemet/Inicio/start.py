from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
import pytz
import os
import json

@Astro("start")
async def start(client, message):
    # Obtener el ID del usuario según si es un chat privado o un grupo
    user_id = message.from_user.id if message.chat.type == 'private' else message.chat.id
    username = message.from_user.username or "Usuario"

    user_data = MondB(idchat=user_id).queryUser()

    if not user_data:
        data, buttons_data = load_language_file(user_id)
        await message.reply_text(
            data['register_not'],
            reply_to_message_id=message.id
        )
        return

    lang = user_data.get("lang", "es").lower()
    data, buttons_data = load_language_file(user_id)

    status = user_data.get("status", "")
    ban_status = "Sí" if status.lower() == "baneado" else "No"

    if status.lower() == "baneado":
        await message.reply_text(
            data['block_message'].format(user_id=user_id),
            reply_to_message_id=message.id
        )
        return

    start_text = data.get("startx", "¡Bienvenido!")
    formatted_text = start_text.format(
        caracas_time=caracas_time(lang),
        username=username,
        idioma_actual=LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')
    )

    mainstart_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("mainstart", [])
    ]

    await message.reply_text(
        formatted_text,
        reply_markup=InlineKeyboardMarkup(mainstart_buttons),
        reply_to_message_id=message.id
    )
