from configs.def_main import *

@ryas("setpriv")
async def set_priv(client, message):
    if message.from_user.id != int(OWNER_ID):
        await message.reply(not_privilegios, reply_to_message_id=message.id)
        return

    try:
        _, user_id, privilegio = message.text.split(" ")
        user_id = int(user_id.strip())
        privilegio = int(privilegio.strip())
    except ValueError:
        await message.reply("Uso correcto: /setpriv <ID> <Privilegio>", reply_to_message_id=message.id)
        return

    conn, cursor = connect_db()

    cursor.execute("SELECT rango, privilegio FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE users SET privilegio = %s WHERE user_id = %s", (privilegio, user_id))
        conn.commit()
        await message.reply(f"✅ Privilegio actualizado correctamente para el ID {user_id}.", reply_to_message_id=message.id)
    else:
        await message.reply("⚠️ Ese ID no se encuentra en la base de datos.", reply_to_message_id=message.id)

    cursor.close()
    conn.close()
