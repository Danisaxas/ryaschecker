from _date import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@AstroButton("^description$")
async def handle_description(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    lang_data, buttons_data = load_language_file(user_id)

    description_text = lang_data.get("description_text", "")
    message = description_text.format(
        username=user.username or user.first_name
    )

    back_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("back", [])
    ]

    await callback_query.message.edit_text(message, reply_markup=InlineKeyboardMarkup(back_buttons))
    await callback_query.answer()
