from _date import *
from datetime import datetime
import pytz

@Astro("Start")
async def start(client, message):
    user_id = message.chat.id
    username = message.from_user.username or "Usuario"
    data = load_language_file(user_id)
    start_text = data.get("startx", "¡Bienvenido!")
    timezone = pytz.timezone("America/Caracas")
    caracas_time = datetime.now(timezone).strftime("%H:%M:%S")
    lang = (data.get("lang") or "es").upper()
    message_text = start_text.format(caracas_time=caracas_time, username=username, idioma_actual=lang)
    await client.send_message(chat_id=user_id, text=message_text)