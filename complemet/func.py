import threading
import time
from classBot.MongoDB import MondB
from datetime import timedelta
import re

def inicializar_expiracion_por_dias(dias: int) -> str:
    if dias <= 0:
        return "0d-00h-00m-00s"
    else:
        dias_restantes = dias - 1
        return f"{dias_restantes}d-23h-59m-59s"

def actualizar_expiracion(idchat: int):
    db = MondB(idchat=idchat)
    user = db.queryUser()
    if not user:
        return False

    dias = user.get("dias", 0)
    expiracion = user.get("expiracion", "0d-00h-00m-00s")

    if expiracion == "0d-00h-00m-00s" and dias > 0:
        expiracion = inicializar_expiracion_por_dias(dias)

    match = re.match(r"(\d+)d-(\d+)h-(\d+)m-(\d+)s", expiracion)
    if match:
        exp_dias = int(match.group(1))
        exp_horas = int(match.group(2))
        exp_minutos = int(match.group(3))
        exp_segundos = int(match.group(4))
    else:
        exp_dias = dias - 1 if dias > 0 else 0
        exp_horas = 23 if dias > 0 else 0
        exp_minutos = 59 if dias > 0 else 0
        exp_segundos = 59 if dias > 0 else 0

    if dias == 0 and exp_dias == 0 and exp_horas == 0 and exp_minutos == 0 and exp_segundos == 0:
        user_collection = db._db['user']
        user_collection.update_one(
            {"_id": idchat},
            {"$set": {
                "expiracion": "0d-00h-00m-00s",
                "dias": 0
            }}
        )
        return True

    tiempo_restante = timedelta(days=exp_dias, hours=exp_horas, minutes=exp_minutos, seconds=exp_segundos)

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

    if dias != nuevo_dias:
        dias = nuevo_dias

    nueva_expiracion = f"{nuevo_dias}d-{nuevo_horas:02d}h-{nuevo_minutos:02d}m-{nuevo_segundos:02d}s"

    user_collection = db._db['user']
    user_collection.update_one(
        {"_id": idchat},
        {"$set": {
            "expiracion": nueva_expiracion,
            "dias": dias
        }}
    )
    return True

def worker_expiracion(interval_seconds=1):
    """
    Loop infinito que actualiza expiracion de todos los usuarios
    cada interval_seconds segundos para que baje continuamente.
    """
    db = MondB()
    user_collection = db._db['user']

    while True:
        try:
            usuarios = user_collection.find({"dias": {"$gte": 0}})
            for user in usuarios:
                actualizar_expiracion(user["_id"])
        except Exception as e:
            print(f"[worker_expiracion] Error: {e}")
        time.sleep(interval_seconds)

def iniciar_expiracion_en_background(interval_seconds=1):
    """
    Inicia worker_expiracion en un hilo daemon para que corra en segundo plano.
    """
    thread = threading.Thread(target=worker_expiracion, args=(interval_seconds,), daemon=True)
    thread.start()
