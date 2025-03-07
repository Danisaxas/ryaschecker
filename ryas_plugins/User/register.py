from configs.def_main import *
import mysql.connector

# Datos de conexión a la base de datos
DB_CONFIG = {
    'host': 'yamabiko.proxy.rlwy.net',
    'port': 11218,
    'user': 'root',
    'password': 'BtXxRgIKxUHvpYfXPLqBWOeAhrAHXfjc',
    'database': 'railway'
}

def connect_db():
    """Conectar a la base de datos y devolver el cursor y la conexión."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    return conn, cursor

def create_users_table():
    """Crea la tabla Users si no existe."""
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id BIGINT PRIMARY KEY,
            rango VARCHAR(50) DEFAULT 'Free User',
            creditos INT DEFAULT 0,
            antispam BOOLEAN DEFAULT FALSE,
            expiracion DATE,
            dias INT DEFAULT 0,
            bin_lasted VARCHAR(255),
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@ryas('register')
def register_user(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    
    conn, cursor = connect_db()
    
    try:
        cursor.execute("INSERT INTO Users (user_id, rango, creditos, antispam, expiracion, dias, bin_lasted, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())", 
                       (user_id, 'Free User', 0, False, None, 0, None))
        conn.commit()
        message.reply_text("✅ Registro exitoso.")
    except mysql.connector.IntegrityError:
        message.reply_text("⚠️ Ya estás registrado.")
    finally:
        cursor.close()
        conn.close()
