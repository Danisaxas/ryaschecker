from configs.def_main import *

@ryas('register')
def register_user(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    lang = message.from_user.language_code or "es"  # Detecta el idioma del usuario

    conn, cursor = connect_db()
    
    try:
        cursor.execute("""
            INSERT INTO users (user_id, rango, privilegio, creditos, antispam, expiracion, dias, bin_lasted, fecha_registro, lang)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)
        """, (user_id, 'Free User', 0, 0, 60, 0, None, None, lang))
        conn.commit()
        
        registro_msg = """
<b>✅ ¡Registro exitoso!</b>
━━━━━━━━━━━━━
👤 <b>Usuario:</b> @{username}  
🆔 <b>ID:</b> {user_id}
🔰 <b>Rango:</b> Free User
💰 <b>Créditos:</b> 0
⏳ <b>Antispam:</b> 60 segundos
📅 <b>Expiración:</b> No aplica
🌍 <b>Idioma:</b> {lang.upper()}
━━━━━━━━━━━━━
🎯 <b>¡Bienvenido a RyasChk!</b> Usa /cmds para ver los comandos disponibles.
""".format(username=username, user_id=user_id, lang=lang)

        message.reply_text(registro_msg)

    except mysql.connector.IntegrityError:
        message.reply_text("<b>⚠️ Ya estás registrado en el sistema.</b>")
    finally:
        cursor.close()
        conn.close()