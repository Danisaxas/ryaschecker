from datetime import datetime, timedelta
import pytz
from classBot.MongoDB import MondB

def guardar_key(key, dias, username):
    venezuela = pytz.timezone("America/Caracas")
    now = datetime.now(pytz.utc).astimezone(venezuela)
    expiracion = now + timedelta(days=dias)

    datos = {
        "key": key,
        "dias": dias,
        "usuario": username,
        "expiracion": expiracion.strftime("%Y-%m-%d %I:%M:%S %p"),
        "fecha": now  # Mongo lo guarda como ISODate
    }

    MondB()._client['bot']['key'].insert_one(datos)
