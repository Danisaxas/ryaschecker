from _date import *
import random
import string
from datetime import datetime, timedelta
import pytz
from classBot.MongoDB import MondB
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("key")
async def key_handler(client, message):
    user_id = message.from_user.id
    user_lang = message.from_user.language_code or 'es'
    user_lang = 'en' if user_lang.startswith('en') else 'es'

    args = message.text.split()

    user = MondB(idchat=user_id).queryUser()
    if user:
        lang = user.get("lang", "es").lower()
        lang = 'en' if lang.startswith('en') else 'es'
    else:
        lang = user_lang

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    if not user:
        await message.reply_text(
            lang_data['block_message'],
            reply_to_message_id=message.id
        )
        return

    role = user.get("role", "User")

    db = MondB()
    rangos_col = db._db['rangos']
    rango_doc = rangos_col.find_one({"Rango": {"$regex": f"^{role}$", "$options": "i"}})

    if not rango_doc:
        await message.reply_text(
            lang_data['block_message'],
            reply_to_message_id=message.id
        )
        return

    numero_rango = rango_doc.get("Numero", 1)

    if numero_rango == 1:
        await message.reply_text(
            lang_data['not_privilegios'],
            reply_to_message_id=message.id
        )
        return

    if len(args) < 2 or not args[1].isdigit():
        await message.reply_text(
            lang_data['key_usage'],
            reply_to_message_id=message.id
        )
        return

    dias = int(args[1])

    key_random = ''.join(random.choices(string.ascii_letters + string.digits + "€#+*", k=8))
    key_generada = f"AstroKey_#{key_random}"

    username = message.from_user.username or "unknown"

    venezuela_tz = pytz.timezone("America/Caracas")
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    now_ven = now_utc.astimezone(venezuela_tz)
    fecha_expiracion = (now_ven + timedelta(days=dias)).strftime("%Y-%m-%d %I:%M:%S %p")

    MondB().save_generated_key(key_generada, dias, username)

    respuesta = lang_data['key_system'].format(
        Key=key_generada,
        date=fecha_expiracion,
        dias=dias,
        username=username
    )

    await message.reply_text(respuesta, reply_to_message_id=message.id)