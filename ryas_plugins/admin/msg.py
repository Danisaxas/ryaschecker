from configs.def_main import *

@ryas("msg")
async def send_message(client, message):
    user_id = message.from_user.id
    conn, cursor = connect_db()

    cursor.execute("SELECT privilegio FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    if not result or result[0] < 3:
        await message.reply(not_privilegios, reply_to_message_id=message.id)
        return

    args = message.text.split(" ", 2)
    if len(args) < 2:
        return

    if args[1].startswith("-"):
        target_id = int(args[1])
        cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (target_id,))
        if cursor.fetchone():
            await client.send_message(target_id, args[2])
    elif args[1].isdigit():
        target_id = int(args[1])
        cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (target_id,))
        if cursor.fetchone():
            await client.send_message(target_id, args[2])
    else:
        cursor.execute("SELECT user_id FROM users")
        users = cursor.fetchall()
        for user in users:
            await client.send_message(user[0], " ".join(args[1:]))
    
    cursor.close()
    conn.close()
