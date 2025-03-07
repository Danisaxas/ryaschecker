from configs.def_main import *
@ryas('me')
async def me_command(client, message):
    user_id = message.from_user.id
    conn, cursor = connect_db()

    cursor.execute("""
        SELECT rango, creditos, antispam, expiracion
        FROM Users
        WHERE user_id = %s
    """, (user_id,))
    user_data = cursor.fetchone()

    if user_data:
        rango, creditos, antispam, expiracion = user_data
        formatted_metext = metext.format(
            username=message.from_user.username,
            user_id=user_id,
            firts_name=message.from_user.first_name,
            rango=rango,
            creditos=creditos,
            antispam=antispam,
            expiracion=expiracion or 'No expiration'
        )
        await message.reply(formatted_metext, reply_to_message_id=message.id)
    else:
        await message.reply(register_not, reply_to_message_id=message.id)
