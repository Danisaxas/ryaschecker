from _date import *

@Astro("key")
async def key_handler(client, message):
    text = message.text
    try:
        key_value = text.split(maxsplit=1)[1]
    except IndexError:
        await message.reply("Por favor envía una clave válida después del comando.")
        return

    respuesta = (
        "¡Clave recibida!\n"
        f"Tu clave es: {key_value}\n"
        "Gracias por usar el sistema de recompensas.\n"
        "Pronto recibirás tu premio."
    )

    await message.reply(respuesta)