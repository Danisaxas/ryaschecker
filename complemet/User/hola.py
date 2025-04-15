from _date import *
import requests

@Astro('hola')
def hola(client, message):
    user_id = message.from_user.id
    user = MondB(idchat=user_id).queryUser()
    lang = user.get("lang")
    texto = "Hola, ¿cómo estás?"
    texto_traducido = texto if lang == "es" else traducir_a_ingles(texto)
    client.send_message(chat_id=user_id, text=texto_traducido)

def traducir_a_ingles(texto):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": "auto", "tl": "en", "dt": "t", "q": texto, "ie": "UTF-8", "oe": "UTF-8"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            return response.json()[0][0][0]
        except Exception:
            return "Error al procesar la respuesta."
    return f"Error en la solicitud: {response.status_code}"
