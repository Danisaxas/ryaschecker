from configs.def_main import *
@ryas('me, info')
def me_command(client, message):
    user_id = message.from_user.id  # Obtén el ID del usuario que ejecuta el comando
    conn, cursor = connect_db()  # Conectamos a la base de datos

    # Consulta para obtener la información del usuario
    cursor.execute("""
        SELECT rango, creditos, antispam, expiracion
        FROM Users
        WHERE user_id = %s
    """, (user_id,))
    user_data = cursor.fetchone()  # Obtener los datos del usuario

    # Si el usuario está registrado
    if user_data:
        rango, creditos, antispam, expiracion = user_data
        # Formatear el texto usando los valores obtenidos
        formatted_metext = metext.format(
            username=message.from_user.username,
            user_id=user_id,
            firts_name=message.from_user.first_name,
            rango=rango,
            creditos=creditos,
            antispam=antispam,
            expiracion=expiracion or 'No expiration'
        )
    else:
        # Si el usuario no está en la base de datos
        formatted_metext = "<b>No se ha encontrado información para este usuario.</b>"

    # Enviar la respuesta al chat
    client.send_message(message.chat.id, formatted_metext)
