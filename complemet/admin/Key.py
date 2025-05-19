from _date import *
import random
import string
from datetime import datetime

@Astro("key")
async def key_handler(client, message):
    text = message.text
    args = text.split()

    if len(args) < 2 or not args[1].isdigit():
        await message.reply("Por favor envía un número de días válido después del comando, ejemplo: Key 2")
        return

    dias = int(args[1])

    key_random = ''.join(random.choices(string.ascii_letters + string.digits + "€#+*", k=8))
    key_generada = f"AstroKey_#{key_random}"

    username = message.from_user.username or "desconocido"
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    respuesta = (
        "Key generated\n"
        "----\n"
        f"Key >> {key_generada}\n"
        f"Días >> {dias}\n"
        f"Claimed by >> @{username}\n"
        f"Date >> {fecha}"
    )

    await message.reply(respuesta)