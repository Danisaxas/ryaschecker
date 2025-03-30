from configs.def_main import * # Importando configuraciones

# Decorador para el comando "me"
@ryas('me')
async def me_command(client, message):
    """
    Muestra la información del usuario que usa el comando.

    Parámetros:
        client: El cliente del bot (ej., Telegram Bot API).
        message: El mensaje que activó el comando.
    """
    user_id = message.from_user.id  # Obteniendo el ID del usuario
    connection, cursor = connect_db()  # Conectando a la base de datos

    # Preparando el query SQL para obtener la información del usuario
    cursor.execute("""
        SELECT rango, creditos, antispam, expiracion
        FROM users
        WHERE user_id = %s
    """, (user_id,))  # Usando una tupla para el parámetro

    user_data = cursor.fetchone()  # Obteniendo los resultados del query

    if user_data:
        # Si encontramos al usuario en la base de datos...
        rango, creditos, antispam, expiration = user_data  # Desempaquetando los datos

        # Formateando el mensaje de respuesta con la información del usuario
        formatted_text = metext.format(  # Asumiendo que 'metext' es un string de formato
            username=message.from_user.username,
            user_id=user_id,
            firts_name=message.from_user.first_name,  # ¡Ojo! 'firts_name' está mal escrito, debería ser 'first_name'
            rango=rango,
            creditos=creditos,
            antispam=antispam,
            expiration=expiration or 'No expiration'  # Si expiration es None, pone "No expiration"
        )
        await message.reply(formatted_text, reply_to_message_id=message.id)
    else:
        # Si no encontramos al usuario en la base de datos...
        await message.reply(register_not, reply_to_message_id=message.id)  # Asumiendo que 'register_not' es el mensaje de error
