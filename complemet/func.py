from classBot.MongoDB import queryUser, MondB

def calcular_rango_por_dias_y_tiempo(user_id: int) -> int:
    user_data = queryUser(user_id)
    if not user_data:
        return 0

    dias = user_data.get("dias", 0)
    time_user = user_data.get("time_user", 0)
    plan = user_data.get("plan", "Free User").lower()

    if dias >= 1 or time_user > 0:
        # Si tiene días o tiempo restante, es rango 7 (Premium)
        return 7
    else:
        # Si no tiene días ni tiempo, es rango 0 (Free)
        return 0

def actualizar_tiempo_usuario(user_id: int):
    db = MondB()
    user_data = queryUser(user_id)
    if not user_data:
        return False

    dias = user_data.get("dias", 0)
    time_user = user_data.get("time_user", 0)

    if dias == 0 and time_user == 0:
        return True

    if time_user == 0 and dias > 0:
        time_user = 86400

    time_user -= 1
    if time_user < 0:
        time_user = 0

    if time_user == 0 and dias > 0:
        dias -= 1
        if dias > 0:
            time_user = 86400
        else:
            time_user = 0

    db._client['bot']['user'].update_one(
        {"_id": user_id},
        {"$set": {"dias": dias, "time_user": time_user}}
    )
    return True
