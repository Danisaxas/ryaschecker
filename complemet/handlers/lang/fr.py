from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@AstroButton("^fr$")
async def set_lang_fr(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    data = "Cloud DB | LANG [🇫🇷] \n\nSuccès ! Votre langue sélectionnée est maintenant [Français] !"

    db = MondB(idchat=user_id)
    db.update_user_lang("fr")

    lang_data, buttons_data = load_language_file(user_id)

    back_lang_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("back_lang", [])
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()
