from configs.def_main import *

@ryas("setpriv")
async def set_priv(client, message):
    if message.from_user.id != int(OWNER_ID):
        await message.reply(not_privilegios, reply_to_message_id=message.id)
        return

    args = message.text.split(" ")
    if len(args) != 3:
        await message.reply(
            "𝗨𝘀𝗼 𝗰𝗼𝗿𝗿𝗲𝗰𝘁𝗼: /setpriv <ID> <Privilegio>",
            reply_to_message_id=message.id
        )
        return

    _, user_id, privilegio = args
    try:
        user_id = int(user_id.strip())
        privilegio = int(privilegio.strip())
    except ValueError:
        await message.reply(
            "𝗘𝗹 𝗜𝗗 𝘆 𝗲𝗹 𝗽𝗿𝗶𝘃𝗶𝗹𝗲𝗴𝗶𝗼 𝗱𝗲𝗯𝗲𝗻 𝘀𝗲𝗿 𝗻𝘂́𝗺𝗲𝗿𝗼𝘀.",
            reply_to_message_id=message.id
        )
        return

    conn, cursor = connect_db()

    cursor.execute("SELECT rango, privilegio FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE users SET privilegio = %s WHERE user_id = %s", (privilegio, user_id))
        conn.commit()
        await message.reply(
            f"𝗣𝗿𝗶𝘃𝗶𝗹𝗲𝗴𝗶𝗼 𝗮𝗰𝘁𝘂𝗮𝗹𝗶𝘇𝗮𝗱𝗼 𝗰𝗼𝗿𝗿𝗲𝗰𝘁𝗮𝗺𝗲𝗻𝘁𝗲 𝗽𝗮𝗿𝗮 𝗲𝗹 𝗜𝗗 {user_id}.",
            reply_to_message_id=message.id
        )
    else:
        await message.reply(
            "𝗘𝘀𝗲 𝗜𝗗 𝗻𝗼 𝘀𝗲 𝗲𝗻𝗰𝘂𝗲𝗻𝘁𝗿𝗮 𝗲𝗻 𝗹𝗮 𝗯𝗮𝘀𝗲 𝗱𝗲 𝗱𝗮𝘁𝗼𝘀.",
            reply_to_message_id=message.id
        )

    cursor.close()
    conn.close()
