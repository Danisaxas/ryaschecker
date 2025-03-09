from configs.def_main import *

@ryas("setpriv")
async def set_priv(client, message):
    if message.from_user.id != int(OWNER_ID):
        await message.reply(not_privilegios, reply_to_message_id=message.id)
        return

    args = message.text.split(" ")
    if len(args) != 3:
        await message.reply("[<a href='https://t.me/ryascheckerbot'>⺢</a>] <b>Uso correcto: /setpriv <ID> <Privilegio></b>", reply_to_message_id=message.id)
        return

    _, user_id, privilegio = args
    try:
        user_id = int(user_id.strip())
        privilegio = int(privilegio.strip())
    except ValueError:
        await message.reply("[<a href='https://t.me/ryascheckerbot'>⺢</a>] <b>El ID y el privilegio deben ser números.</b>", reply_to_message_id=message.id)
        return

    conn, cursor = connect_db()

    cursor.execute("SELECT rango, privilegio FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE users SET privilegio = %s WHERE user_id = %s", (privilegio, user_id))
        conn.commit()
        await message.reply(f"[<a href='https://t.me/ryascheckerbot'>⺢</a>] <b>Privilegio actualizado correctamente para el ID {user_id}.</b>", reply_to_message_id=message.id)
    else:
        await message.reply("[<a href='https://t.me/ryascheckerbot'>⺢</a>] <b>Ese ID no se encuentra en la base de datos.</b>", reply_to_message_id=message.id)

    cursor.close()
    conn.close()