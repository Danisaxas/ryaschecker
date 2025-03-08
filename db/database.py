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
    """Crea la tabla users si no existe."""
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            rango VARCHAR(50) DEFAULT 'Free User',
            privilegio INT DEFAULT 0,  -- Se coloca privilegio después de rango
            creditos INT DEFAULT 0,
            antispam BOOLEAN DEFAULT FALSE,
            expiracion DATE,
            dias INT DEFAULT 0,
            bin_lasted VARCHAR(255),
            ban VARCHAR(3) DEFAULT 'No',  -- Se añade la columna ban al lado de bin_lasted
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            lang VARCHAR(10) DEFAULT 'es'  -- Se coloca lang al final
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@ryas('register')
def register_user(self, message):
    """Comando para registrar un usuario en la base de datos."""
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    
    conn, cursor = connect_db()
    
    try:
        cursor.execute("INSERT INTO users (user_id, rango, privilegio, creditos, antispam, expiracion, dias, bin_lasted, ban, fecha_registro, lang) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)", 
                       (user_id, 'Free User', 0, 0, False, None, 0, None, 'No', 'es'))  # Se incluyen las columnas lang y privilegio
        conn.commit()
        message.reply_text("✅ Registro exitoso.")
    except mysql.connector.IntegrityError:
        message.reply_text("⚠️ Ya estás registrado.")
    finally:
        cursor.close()
        conn.close()

# Crear la tabla users al iniciar el script
create_users_table()
