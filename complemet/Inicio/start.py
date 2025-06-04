from _date import *
from classBot.MongoDB import MondB
from datetime import datetime
import pytz

@Astro("start")
async def start(client, message):
    user_id = message.chat.id
    username = message.from_user.username or "Usuario"

    data, buttons_data = load_language_file(user_id)

    start_text = data.get("startx", "¡Bienvenido!")

    mainstart_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("mainstart", [])
    ]

    timezone = pytz.timezone("America/Caracas")
    caracas_time = datetime.now(timezone).strftime("%H:%M:%S")

    # Usar directamente el resultado de queryUser() para obtener el idioma
    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    idioma_actual = f"{LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')} {lang.upper()}"

    message_text = start_text.format(caracas_time=caracas_time, username=username, idioma_actual=idioma_actual)

    # Usar message.id para la respuesta
    reply_to_message_id = message.id  # Utiliza message.id para responder al mensaje actual

    await client.send_message(
        chat_id=user_id,
        text=message_text,
        reply_markup=InlineKeyboardMarkup(mainstart_buttons),
        reply_to_message_id=reply_to_message_id  # Responde al mensaje original con el comando /start
    )
