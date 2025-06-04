from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(level=logging.INFO)

@AstroButton("^ryas_cloud$")
async def handle_xcloud(client, callback_query):
    try:
        user = callback_query.from_user
        user_id = user.id

        logging.info(f"Button pressed by user: {user.username or user.first_name}, User ID: {user_id}")

        user_data = MondB(idchat=user_id).queryUser()
        lang = (user_data.get("lang") if user_data else "es") or "es"
        lang = lang.lower()

        data, buttons_data = load_language_file(user_id)

        ryas_cloud_template = data.get("ryas_cloud", "")
        message = ryas_cloud_template.format(
            username=user.username or user.first_name
        )

        vryasx_buttons = [
            [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
            for row in buttons_data.get("vryasx", [])
        ]

        await callback_query.message.edit_text(message, reply_markup=InlineKeyboardMarkup(vryasx_buttons))
        await callback_query.answer()

        logging.info("Successfully updated message with xCloud buttons.")

    except Exception as e:
        logging.error(f"Error handling 'ryas_cloud' button: {e}")
        await callback_query.answer("Ocurrió un error al procesar el botón.", show_alert=True)
