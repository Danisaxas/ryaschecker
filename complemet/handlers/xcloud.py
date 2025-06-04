from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@AstroButton("^ryas_cloud$")
async def handle_xcloud(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    data, buttons_data = load_language_file(user_id)

    ryas_cloud_template = data.get("ryas_cloud", "")
    idioma_actual = LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')  # Agregar idioma actual
    message = ryas_cloud_template.format(
        username=user.username or user.first_name,
        idioma_actual=idioma_actual  # Pasar el idioma actual a la plantilla
    )

    vryasx_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("vryasx", [])
    ]

    await callback_query.message.edit_text(message, reply_markup=InlineKeyboardMarkup(vryasx_buttons))
    await callback_query.answer()
