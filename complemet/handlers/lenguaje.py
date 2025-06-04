from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@AstroButton("^lenguaje$")
async def handle_lenguaje(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    data, buttons_data = load_language_file(user_id)

    lang_message = data.get("lang_message", "")
    message = lang_message.format(
        username=user.username or user.first_name,
        idioma_actual=LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')
    )

    lang_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("lang", [])
    ]

    await callback_query.message.edit_text(message, reply_markup=InlineKeyboardMarkup(lang_buttons))
    await callback_query.answer()
