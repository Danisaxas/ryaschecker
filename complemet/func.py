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

def actualizar_expiracion_si_necesario(user_id: int):
    db = MondB()
    user = queryUser(user_id)
    if not user:
        return None

    dias = user.get("dias", 0)
    since = user.get("since")
    now = datetime.now(timezone.utc)

    if not since:
        return None

    if isinstance(since, str):
        since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
    else:
        since_dt = since

    # Calcular tiempo total permitido
    tiempo_total = timedelta(days=dias)

    # Tiempo pasado desde 'since'
    tiempo_pasado = now - since_dt

    # Tiempo restante
    tiempo_restante = tiempo_total - tiempo_pasado

    # Si el tiempo restante es negativo o 0, poner dias a 0 y expiracion en 0
    if tiempo_restante.total_seconds() <= 0:
        db._client['bot']['user'].update_one(
            {"_id": user_id},
            {"$set": {"dias": 0, "expiracion": "0d-00h-00m-00s"}}
        )
        return

    # Actualizar expiracion como string en formato deseado
    expiracion_str = formato_tiempo(tiempo_restante)
    db._client['bot']['user'].update_one(
        {"_id": user_id},
        {"$set": {"expiracion": expiracion_str}}
    )
