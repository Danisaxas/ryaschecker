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

def obtener_rango_por_numero(numero: int) -> str:
    db = MondB()
    rango_doc = db._db['rangos'].find_one({"Numero": numero})
    if rango_doc and "Rango" in rango_doc:
        return rango_doc["Rango"]
    return "Free"

def actualizar_plan_por_dias(idchat: int, dias: int):
    rango_nombre = obtener_rango_por_numero(7 if dias > 0 else 0)
    db = MondB(idchat=idchat)
    user = db.queryUser()
    if not user:
        return False
    if user.get("plan", "") != rango_nombre:
        db._db['user'].update_one({"_id": idchat}, {"$set": {"plan": rango_nombre}})
    return True

def actualizar_expiracion(idchat: int, nuevo_dias_param: int = None):
    db = MondB(idchat=idchat)
    user = db.queryUser()
    if not user:
        return False

    dias_bd = user.get("dias", 0)
    expiracion = user.get("expiracion", "0d-00h-00m-00s")

    # Reinicia expiracion si nuevo_dias_param llega distinto
    if nuevo_dias_param is not None and nuevo_dias_param != dias_bd:
        dias_bd = nuevo_dias_param
        expiracion = inicializar_expiracion_por_dias(dias_bd)
        db._db['user'].update_one({"_id": idchat}, {"$set": {"dias": dias_bd, "expiracion": expiracion}})
        actualizar_plan_por_dias(idchat, dias_bd)
        return True

    # Si expiracion no está sincronizada con dias_bd, reiniciar expiracion
    match = re.match(r"(\d+)d-(\d+)h-(\d+)m-(\d+)s", expiracion)
    if not match:
        expiracion = inicializar_expiracion_por_dias(dias_bd)
        db._db['user'].update_one({"_id": idchat}, {"$set": {"expiracion": expiracion}})
        match = re.match(r"(\d+)d-(\d+)h-(\d+)m-(\d+)s", expiracion)
    else:
        exp_dias = int(match.group(1))
        # Si expiracion indica menos días que dias_bd, reiniciar expiracion
        if exp_dias + 1 < dias_bd:  # +1 porque expiracion cuenta días restantes menos 1
            expiracion = inicializar_expiracion_por_dias(dias_bd)
            db._db['user'].update_one({"_id": idchat}, {"$set": {"expiracion": expiracion}})
            match = re.match(r"(\d+)d-(\d+)h-(\d+)m-(\d+)s", expiracion)

    exp_dias = int(match.group(1))
    exp_horas = int(match.group(2))
    exp_minutos = int(match.group(3))
    exp_segundos = int(match.group(4))

    tiempo_restante = timedelta(days=exp_dias, hours=exp_horas, minutes=exp_minutos, seconds=exp_segundos)

    if tiempo_restante.total_seconds() > 0:
        tiempo_restante -= timedelta(seconds=2)
    else:
        tiempo_restante = timedelta(0)

    total_segundos = int(tiempo_restante.total_seconds())

    nuevo_dias = total_segundos // 86400
    resto = total_segundos % 86400

    nuevo_horas = resto // 3600
    nuevo_minutos = (resto % 3600) // 60
    nuevo_segundos = resto % 60

    nueva_expiracion = f"{max(nuevo_dias,0)}d-{nuevo_horas:02d}h-{nuevo_minutos:02d}m-{nuevo_segundos:02d}s"

    # Si el día de expiracion pasó a menos que antes, descontar un día de dias_bd
    if exp_dias > nuevo_dias and dias_bd > 0:
        dias_bd -= 1
        if dias_bd < 0:
            dias_bd = 0
        db._db['user'].update_one({"_id": idchat}, {"$set": {"dias": dias_bd}})

    db._db['user'].update_one({"_id": idchat}, {"$set": {"expiracion": nueva_expiracion}})

    actualizar_plan_por_dias(idchat, dias_bd)

    return True

def worker_expiracion(interval_seconds=1):
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
    thread = threading.Thread(target=worker_expiracion, args=(interval_seconds,), daemon=True)
    thread.start()
