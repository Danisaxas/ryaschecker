from configs.def_main import * # Importando configuraciones

@ryas("gen")
async def gen_command(client, message):
    """
    Muestra información sobre el generador de tarjetas al usar el comando .gen.
    """
    respuesta = (
        "• »  Tool: GENERATOR CARDS GENERATOR\n"
        "• »  Status: On ? | Plan: FREE\n"
        "• »  Usage: $gen bin|mm|yy|cvv|amount"
    )
    await message.reply(respuesta, reply_to_message_id=message.id)
