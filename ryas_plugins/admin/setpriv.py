from configs.def_main import *

@ryas("setpriv")
def set_priv(client, message):
    if message.from_user.id != int(OWNER_ID):
        message.reply(Not_permission)
        return

    try:
        _, user_id, privilegio = message.text.split(" ")
        user_id = int(user_id.strip())
        privilegio = int(privilegio.strip())
    except ValueError:
        message.reply("Uso correcto: /setpriv <ID> <Privilegio>")
        return

    conn, cursor = connect_db()

    cursor.execute("SELECT rango, privilegio FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE users SET privilegio = %s WHERE user_id = %s", (privilegio, user_id))
        conn.commit()
        message.reply(f"✅ Privilegio actualizado correctamente para el ID {user_id}.")
    else:
        message.reply("⚠️ Ese ID no se encuentra en la base de datos.")

    cursor.close()
    conn.close()
