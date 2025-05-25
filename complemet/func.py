import time
import schedule
from datetime import datetime, timedelta, timezone
from classBot.MongoDB import MondB, queryUser

def formato_tiempo(delta: timedelta) -> str:
    total_segundos = int(delta.total_seconds())
    if total_segundos <= 0:
        return "0d-00h-00m-00s"
    dias = total_segundos // 86400
    horas = (total_segundos % 86400) // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return f"{dias}d-{horas:02d}h-{minutos:02d}m-{segundos:02d}s"

def actualizar_expiracion_usuario(user):
    user_id = user.get('_id')
    dias = user.get("dias", 0)
    since = user.get("since")
    now = datetime.now(timezone.utc)
    if not since or dias <= 0:
        MondB()._client['bot']['user'].update_one(
            {"_id": user_id},
            {"$set": {"dias": 0, "expiracion": "0d-00h-00m-00s"}}
        )
        return
    if isinstance(since, str):
        since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
    else:
        since_dt = since
    tiempo_total = timedelta(days=dias)
    tiempo_pasado = now - since_dt
    tiempo_restante = tiempo_total - tiempo_pasado
    if tiempo_restante.total_seconds() <= 0:
        MondB()._client['bot']['user'].update_one(
            {"_id": user_id},
            {"$set": {"dias": 0, "expiracion": "0d-00h-00m-00s"}}
        )
        return
    expiracion_str = formato_tiempo(tiempo_restante)
    MondB()._client['bot']['user'].update_one(
        {"_id": user_id},
        {"$set": {"expiracion": expiracion_str}}
    )

def actualizar_todas_expiraciones():
    db = MondB()
    usuarios = db._db['user'].find({"dias": {"$gt": 0}})
    for user in usuarios:
        actualizar_expiracion_usuario(user)

def iniciar_scheduler(time_interval_seconds=1):
    schedule.every(time_interval_seconds).seconds.do(actualizar_todas_expiraciones)
    while True:
        schedule.run_pending()
        time.sleep(0.5)
