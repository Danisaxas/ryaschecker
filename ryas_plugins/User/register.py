from configs.def_main import *
from db.database import connect_db
import mysql.connector
@ryas('register')
def register_user(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    
    conn, cursor = connect_db()
    
    try:
        cursor.execute("""
            INSERT INTO Users (user_id, rango, creditos, antispam, expiracion, dias, bin_lasted, fecha_registro)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
        """, (user_id, 'Free User', 0, False, None, 0, None))
        conn.commit()
        message.reply_text("✅ Registro exitoso.")
    except mysql.connector.IntegrityError:
        message.reply_text("⚠️ Ya estás registrado.")
    finally:
        cursor.close()
        conn.close()