from configs.def_main import *
@ryas("start")
async def start(client, msg):
    username = msg.from_user.username or "Usuario"
    
    # Obtener la fecha y hora actual en Caracas, Venezuela con el formato correcto
    caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")

    # Generar el mensaje
    response = startx.format(username=username, caracas_time=caracas_time)

    await msg.reply_text(
        response,
        reply_to_message_id=msg.id,
        reply_markup=mainstart
    )
