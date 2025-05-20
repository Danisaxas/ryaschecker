from _date import *
import random
import string
from datetime import datetime, timedelta
import pytz
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from classBot.MongoDB import MondB

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

    text_dict = text_en if lang == "en" else text_es

    if not user:
        await message.reply_text(
            "<b>Access denied. You are not registered.</b>" if lang == 'en' else "<b>Acceso denegado. No estás registrado.</b>",
            reply_to_message_id=message.id
        )
        return

    role = user.get("role", "User")

    db = MondB()
    rangos_col = db._db['rangos']
    rango_doc = rangos_col.find_one({"Rango": {"$regex": f"^{role}$", "$options": "i"}})

    if not rango_doc:
        await message.reply_text(
            "<b>Access denied. Your role is not recognized.</b>" if lang == 'en' else "<b>Acceso denegado. Tu rol no está reconocido.</b>",
            reply_to_message_id=message.id
        )
        return

    numero_rango = rango_doc.get("Numero", 1)

    if numero_rango == 1:
        await message.reply_text(
            "<b>Access denied. Your rank cannot use this command.</b>" if lang == 'en' else "<b>Acceso denegado. Tu rango no puede usar este comando.</b>",
            reply_to_message_id=message.id
        )
        return

    if len(args) < 2 or not args[1].isdigit():
        await message.reply_text(text_dict['key_usage'], reply_to_message_id=message.id)
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

    respuesta = text_dict['key_system'].format(
        Key=key_generada,
        date=fecha_expiracion,
        días=dias,
        username=username
    )

    await message.reply_text(respuesta, reply_to_message_id=message.id)
