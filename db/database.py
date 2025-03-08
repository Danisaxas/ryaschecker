import mysql.connector

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
