from pyrogram.types import Message
from _date import *
import json
import os

def mitad(numero):
    return numero / 2

@Astro("mt")
async def comando_mt(client, message: Message):
    user_id = message.from_user.id
    user = MondB(idchat=user_id).queryUser()

    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()
    
    data, buttons_data = load_language_file(user_id)
    
    if not user:
        await message.reply_text(
            data['register_not'],
            reply_to_message_id=message.id
        )
        return
    
    status = user.get("status", "")
    ban_status = "Sí" if status.lower() == "baneado" else "No"

    if status.lower() == "baneado":
        await message.reply_text(
            data['block_message'].format(user_id=user_id),
            reply_to_message_id=message.id
        )
        return

    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.reply_text(data['mt_usage'], reply_to_message_id=message.id)
        return

    try:
        numero = float(args[1])
        resultado = mitad(numero)
        if resultado.is_integer():
            resultado = int(resultado)
        await message.reply_text(
            data['mt_result'].format(numero=int(numero), resultado=resultado),
            reply_to_message_id=message.id
        )
    except ValueError:
        await message.reply_text(data['mt_invalid'], reply_to_message_id=message.id)
