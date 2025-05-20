from datetime import datetime, timedelta, timezone
from classBot.MongoDB import MondB, queryUser

def actualizar_expiracion_si_necesario(user_id: int):
    db = MondB()
    user = queryUser(user_id)
    if not user:
        return None

    dias = user.get("dias", 0)
    expiracion = user.get("expiracion")
    since = user.get("since")
    now = datetime.now(timezone.utc)

    if not since:
        return None

    if isinstance(since, str):
        since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
    else:
        since_dt = since

    if dias > 0:
        if expiracion is None:
            nueva_expiracion = since_dt + timedelta(days=dias)
            db._client['bot']['user'].update_one(
                {"_id": user_id},
                {"$set": {"expiracion": nueva_expiracion}}
            )
        else:
            if isinstance(expiracion, str):
                expiracion_dt = datetime.fromisoformat(expiracion.replace("Z", "+00:00"))
            else:
                expiracion_dt = expiracion

            if expiracion_dt <= now:
                nuevos_dias = max(dias - 1, 0)
                nuevo_since = now if nuevos_dias > 0 else since_dt
                db._client['bot']['user'].update_one(
                    {"_id": user_id},
                    {"$set": {"dias": nuevos_dias, "since": nuevo_since}}
                )
                if nuevos_dias > 0:
                    nueva_expiracion = nuevo_since + timedelta(days=nuevos_dias)
                    db._client['bot']['user'].update_one(
                        {"_id": user_id},
                        {"$set": {"expiracion": nueva_expiracion}}
                    )
                else:
                    db._client['bot']['user'].update_one(
                        {"_id": user_id},
                        {"$set": {"expiracion": None}}
                    )
    else:
        if expiracion is not None:
            db._client['bot']['user'].update_one(
                {"_id": user_id},
                {"$set": {"expiracion": None}}
            )

def tiempo_restante(user_id: int):
    actualizar_expiracion_si_necesario(user_id)
    user = queryUser(user_id)
    if not user:
        return None

    expiracion = user.get("expiracion")
    now = datetime.now(timezone.utc)

    if not expiracion:
        return {"dias": 0, "horas": 0, "minutos": 0, "segundos": 0}

    if isinstance(expiracion, str):
        expiracion_dt = datetime.fromisoformat(expiracion.replace("Z", "+00:00"))
    else:
        expiracion_dt = expiracion

    delta = expiracion_dt - now
    if delta.total_seconds() <= 0:
        return {"dias": 0, "horas": 0, "minutos": 0, "segundos": 0}

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
