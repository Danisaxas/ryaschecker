from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@AstroButton("^en$")
async def set_lang_en(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    data = "Cloud DB | LANG [🇺🇸] \n\nSuccess! Your selected language is now [English]!"

    db = MondB(idchat=user_id)
    db.update_user_lang("en")

    buttons_data = [
        {"text": "xCloud [☁️]", "callback_data": "homevR"},
        {"text": "Languages", "callback_data": "lenguaje"}
    ]

    back_lang_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in buttons_data]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()
