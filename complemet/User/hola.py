from _date import *

@Astro('hola')
def hola(client, message):
    user_id = message.from_user.id
    user = MondB(idchat=user_id).queryUser()
    lang = user.get("lang")
    texto = textas
    texto_traducido = texto if lang == "es" else traducir_a_ingles(texto)
    client.send_message(chat_id=user_id, text=texto_traducido)
