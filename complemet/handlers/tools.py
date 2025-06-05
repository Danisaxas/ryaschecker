from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@AstroButton("^tools$")
async def handle_tools(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    lang_data, buttons_data = load_language_file(user_id)

    tools_text = lang_data.get("tools", "")
    message = tools_text.format(
        username=user.username or user.first_name
    )

    atras_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("atras", [])
    ]

    await callback_query.message.edit_text(message, reply_markup=InlineKeyboardMarkup(atras_buttons))
    await callback_query.answer()

@AstroButton("^next$")
async def handle_next(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    lang_data, buttons_data = load_language_file(user_id)

    tools_2_text = lang_data.get("tools_2", "")
    message = tools_2_text.format(
        username=user.username or user.first_name
    )

    tools_back_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("tools_back", [])
    ]

    await callback_query.message.edit_text(message, reply_markup=InlineKeyboardMarkup(tools_back_buttons))
    await callback_query.answer()
