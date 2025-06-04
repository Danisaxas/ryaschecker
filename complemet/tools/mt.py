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

    if not user:
        text_data = load_language_data("es")
        if not text_data:
            text_data = {}
        await message.reply_text(text_data.get('register_not', "No estás registrado."), reply_to_message_id=message.id)
        return

    lang = (user.get("lang") or "es").lower()
    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    status = user.get("status", "").lower()
    if status == "ban":
        await message.reply_text(
            lang_data['block_message'].format(
                user_id=user_id,
                razon=user.get("razon", "No especificada")
            ),
            reply_to_message_id=message.id
        )
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply_text(lang_data['mt_usage'], reply_to_message_id=message.id)
        return

    try:
        numero = float(args[1])
        resultado = mitad(numero)
        if resultado.is_integer():
            resultado = int(resultado)
        await message.reply_text(
            lang_data['mt_result'].format(numero=numero, resultado=resultado),
            reply_to_message_id=message.id
        )
    except ValueError:
        await message.reply_text(lang_data['mt_invalid'], reply_to_message_id=message.id)
