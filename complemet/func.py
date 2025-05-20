from datetime import datetime, timedelta, timezone
from classBot.MongoDB import MondB, queryUser

def tiempo_restante(user_id: int):
    user = queryUser(user_id)
    if not user:
        return None

    since = user.get("since")
    dias = user.get("dias", 0)
    if not since or dias == 0:
        return {
            "dias": 0,
            "horas": 0,
            "minutos": 0,
            "segundos": 0
        }

    if isinstance(since, str):
        since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
    else:
        since_dt = since

    now = datetime.now(timezone.utc)
    expiration = since_dt + timedelta(days=dias)

    delta = expiration - now
    if delta.total_seconds() <= 0:
        return {
            "dias": 0,
            "horas": 0,
            "minutos": 0,
            "segundos": 0
        }

    dias_restantes = delta.days
    segundos_restantes = delta.seconds
    horas = segundos_restantes // 3600
    minutos = (segundos_restantes % 3600) // 60
    segundos = segundos_restantes % 60

    return {
        "dias": dias_restantes,
        "horas": horas,
        "minutos": minutos,
        "segundos": segundos
    }
