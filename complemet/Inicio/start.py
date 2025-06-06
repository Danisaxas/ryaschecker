from _date import *
from classBot.MongoDB import MondB
from datetime import datetime
import pytz

@Astro("start")
async def start(client, message: Message):
    user_id = message.chat.id
    username = message.from_user.username or "Usuario"

    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    data, buttons_data = load_language_file(user_id)

    if not user_data or user_data.get('_id') != user_id:
        await message.reply_text(
            data['register_not'],
            reply_to_message_id=message.id
        )
        return

    status = user_data.get("status", "")
    if status.lower() == "baneado":
        await message.reply_text(
            data['block_message'].format(user_id=user_id),
            reply_to_message_id=message.id
        )
        return

    start_text = data.get("startx", "¡Bienvenido!")
    mainstart_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("mainstart", [])
    ]

    idioma_actual = f"{LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')}"
    caracas_time_value = caracas_time(lang)

    message_text = start_text.format(caracas_time=caracas_time_value, username=username, idioma_actual=idioma_actual)

    reply_to_message_id = message.id

    await client.send_message(
        chat_id=user_id,
        text=message_text,
        reply_markup=InlineKeyboardMarkup(mainstart_buttons),
        reply_to_message_id=reply_to_message_id
    )
