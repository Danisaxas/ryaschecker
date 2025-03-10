from configs.def_main import *
from ryas_templates.chattext import not_privilegios

@ryas("msg")
async def send_message(client, message):
    user_id = message.from_user.id
    conn, cursor = connect_db()

    cursor.execute("SELECT privilegio FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    if not result or result[0] < 3:
        await message.reply(not_privilegios, reply_to_message_id=message.id)
        return

    if message.reply_to_message:
        forwa_message = message.reply_to_message
    else:
        args = message.text.split(" ", 2)
        if len(args) < 2:
            await message.reply("Admin panel = /msg id or (message)", reply_to_message_id=message.id)
            return

        msg_text = args[1] if len(args) == 2 else args[2]

        if args[1].startswith("-") or args[1].isdigit():
            target_id = int(args[1])
            cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (target_id,))
            if cursor.fetchone():
                await client.forward_messages(target_id, message.chat.id, message.id)
        else:
            cursor.execute("SELECT user_id FROM users")
            users = cursor.fetchall()
            for user in users:
                await client.send_message(user[0], msg_text)
            cursor.close()
            conn.close()
            return

    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    for user in users:
        await client.forward_messages(user[0], message.chat.id, forwa_message.id)

    cursor.close()
    conn.close()
