from configs.def_main import *
import mysql.connector
from ryas import ryas  # Importar ryas para definir el comando

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
            creditos INT DEFAULT 0,
            antispam BOOLEAN DEFAULT FALSE,
            expiracion DATE,
            dias INT DEFAULT 0,
            bin_lasted VARCHAR(255),
            ban VARCHAR(3) DEFAULT 'No',  -- Se añade la columna ban al lado de bin_lasted
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def create_privilegio_table():
    """Crea la tabla privilegio si no existe."""
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS privilegio (
            user_id BIGINT PRIMARY KEY,
            privilegio INT DEFAULT 0  -- Se asigna 0 como valor por defecto
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def create_lang_table():
    """Crea la tabla lang si no existe."""
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lang (
            user_id BIGINT PRIMARY KEY,
            lang VARCHAR(10) DEFAULT 'es'  -- Se asigna 'es' como valor por defecto
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
        cursor.execute("INSERT INTO users (user_id, rango, creditos, antispam, expiracion, dias, bin_lasted, ban, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())", 
                       (user_id, 'Free User', 0, False, None, 0, None, 'No'))  # Se incluye la columna ban
        cursor.execute("INSERT INTO privilegio (user_id, privilegio) VALUES (%s, %s)", (user_id, 0))  # Insertar en la tabla privilegio
        cursor.execute("INSERT INTO lang (user_id, lang) VALUES (%s, %s)", (user_id, 'es'))  # Insertar en la tabla lang
        conn.commit()
        message.reply_text("✅ Registro exitoso.")
    except mysql.connector.IntegrityError:
        message.reply_text("⚠️ Ya estás registrado.")
    finally:
        cursor.close()
        conn.close()

# Crear las tablas al iniciar el script
create_users_table()
create_privilegio_table()
create_lang_table()
