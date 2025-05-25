from datetime import timedelta
import re
from classBot.MongoDB import MondB

def actualizar_expiracion(idchat: int):
    db = MondB(idchat=idchat)
    user = db.queryUser()
    if not user:
        return False  # Usuario no encontrado

    dias = user.get("dias", 0)
    expiracion = user.get("expiracion", "0d-00h-00m-00s")

    # Extraer valores de expiracion
    match = re.match(r"(\d+)d-(\d+)h-(\d+)m-(\d+)s", expiracion)
    if match:
        exp_dias = int(match.group(1))
        exp_horas = int(match.group(2))
        exp_minutos = int(match.group(3))
        exp_segundos = int(match.group(4))
    else:
        exp_dias = dias
        exp_horas = 23
        exp_minutos = 59
        exp_segundos = 59

    # Si ya expiró todo
    if dias == 0 and exp_dias == 0 and exp_horas == 0 and exp_minutos == 0 and exp_segundos == 0:
        return True

    # Tiempo restante como timedelta
    tiempo_restante = timedelta(days=exp_dias, hours=exp_horas, minutes=exp_minutos, seconds=exp_segundos)

    # Descontar 1 segundo
    if tiempo_restante.total_seconds() > 0:
        tiempo_restante -= timedelta(seconds=1)
    else:
        tiempo_restante = timedelta(0)

    total_segundos = int(tiempo_restante.total_seconds())
    nuevo_dias = total_segundos // 86400
    resto = total_segundos % 86400
    nuevo_horas = resto // 3600
    resto = resto % 3600
    nuevo_minutos = resto // 60
    nuevo_segundos = resto % 60

    # Actualizamos campo "dias" si cambio
    if dias != nuevo_dias:
        dias = nuevo_dias

    nueva_expiracion = f"{nuevo_dias}d-{nuevo_horas:02d}h-{nuevo_minutos:02d}m-{nuevo_segundos:02d}s"

    # Actualizamos la base de datos
    user_collection = db._db['user']
    user_collection.update_one(
        {"_id": idchat},
        {"$set": {
            "expiracion": nueva_expiracion,
            "dias": dias
        }}
    )
    return True
