from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from _date import *  # Importamos todo de _date
from classBot.MongoDB import MondB  # Importamos tu clase de base de datos

# Comando que se ejecutará cuando el usuario escriba /start
@Astro("start")
async def start(client, message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Consultamos la base de datos para obtener el idioma del usuario
    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()

    # Cargamos los archivos de idioma
    data, buttons_data = load_language_file(user_id)

    # Obtenemos el texto de bienvenida
    start_text = data.get("startx", "¡Bienvenido!")
    formatted_text = start_text.format(
        caracas_time=caracas_time(lang),
        username=username,
        idioma_actual=LANGUAGES_FLAGS.get(lang, '🏳️‍🌈')
    )

    # Cargamos los botones para el mensaje
    mainstart_buttons = [
        [InlineKeyboardButton(button['text'], callback_data=button['callback_data']) for button in row]
        for row in buttons_data.get("mainstart", [])
    ]

    # Enviamos el mensaje con el texto formateado (sin parse_mode="html") y los botones inline
    await client.send_message(
        chat_id=user_id,
        text=formatted_text,
        reply_markup=InlineKeyboardMarkup(mainstart_buttons)
    )
