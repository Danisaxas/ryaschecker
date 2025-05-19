from _date import *
import random
import string
from datetime import datetime, timedelta
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es

@Astro("key")
async def key_handler(client, message):
    user_id = message.from_user.id
    user_lang = message.from_user.language_code or 'es'
    user_lang = 'en' if user_lang.startswith('en') else 'es'

    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.reply("Please send a valid number of days after the command, example: Key 2" if user_lang == 'en' else "Por favor envía un número válido de días después del comando, ejemplo: Key 2")
        return

    dias = int(args[1])

    key_random = ''.join(random.choices(string.ascii_letters + string.digits + "€#+*", k=8))
    key_generada = f"AstroKey_#{key_random}"

    username = message.from_user.username or "unknown"
    fecha_expiracion = (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%d %H:%M:%S")

    user = MondB(idchat=user_id).queryUser()
    lang = 'es'
    if user:
        lang = user.get('language', 'es')
    else:
        lang = user_lang

    text_dict = text_en if lang == "en" else text_es

    respuesta = text_dict['key_system'].format(
        Key=key_generada,
        date=fecha_expiracion,
        días=dias,
        username=username
    )

    await message.reply(respuesta, reply_to_message_id=message.id)