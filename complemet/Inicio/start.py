from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from _date import *
from classBot.MongoDB import MondB

@Astro("start")
async def start(client, message):
    user_id = message.from_user.id
    username = message.from_user.username

    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()

    data, buttons_data = load_language_file(user_id)

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
        reply_to_message_id=message.id,
        reply_markup=InlineKeyboardMarkup(mainstart_buttons)
    )
