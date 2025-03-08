from configs.def_main import *
@ryas("start")
async def start(client, message):
    user_id = message.from_user.id
    conn, cursor = connect_db()

    cursor.execute("""
        SELECT rango, creditos, antispam, expiracion
        FROM users
        WHERE user_id = %s
    """, (user_id,))
    user_data = cursor.fetchone()

    if not user_data:
        await message.reply(register_not, reply_to_message_id=message.id)
        return

    username = message.from_user.username or "Usuario"
    caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")
    response = startx.format(username=username, caracas_time=caracas_time)

    await message.reply_text(
        response,
        reply_to_message_id=message.id,
        reply_markup=mainstart
    )
