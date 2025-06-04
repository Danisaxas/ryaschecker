import json
import os
from _date import *
from classBot.MongoDB import MondB
from datetime import datetime
import pytz

@Astro("Start")
async def start(update, context):
    user_id = update.effective_chat.id
    username = update.effective_user.username or "Usuario"

    # Obtener idioma del usuario desde la base de datos
    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()

    # Ruta del archivo de idioma
    base_path = os.path.dirname(os.path.abspath(__file__))
    locales_path = os.path.join(base_path, "..", "..", "Locales")
    lang_file = os.path.join(locales_path, f"{lang}.json")

    # Cargar archivo JSON del idioma
    try:
        with open(lang_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        # En caso de error cargar español por defecto
        with open(os.path.join(locales_path, "es.json"), "r", encoding="utf-8") as f:
            data = json.load(f)

    # Obtener el texto de startx
    start_text = data.get("startx", "¡Bienvenido!")

    # Obtener hora de Caracas para variable caracas_time
    timezone = pytz.timezone("America/Caracas")
    caracas_time = datetime.now(timezone).strftime("%H:%M:%S")

    # Preparar idioma_actual para mostrar (puedes personalizar nombres si quieres)
    idioma_actual = lang.upper()

    # Formatear texto con variables
    message = start_text.format(caracas_time=caracas_time, username=username, idioma_actual=idioma_actual)

    # Enviar mensaje sin parse_mode
    await context.bot.send_message(chat_id=user_id, text=message)