import logging
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from _date import *
from classBot.MongoDB import MondB

logging.basicConfig(level=logging.INFO)

@Astro("start")
async def start(client, message):
    try:
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

        if message.chat.type == "private":
            await message.reply_text(
                formatted_text,
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(mainstart_buttons)
            )
        else:
            logging.info(f"Comando start recibido en un grupo: {message.chat.title}, usuario: {username}")

    except Exception as e:
        logging.error(f"Error en el comando /start: {e}", exc_info=True)
        await message.reply_text("Hubo un error al procesar el comando. Intenta nuevamente más tarde.")
