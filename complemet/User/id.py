from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import Message
import json
import os

@Astro('id')
async def obtener_id(client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username or "No username"

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

    status = user.get("status", "").lower()
    if status == 'ban':
        await message.reply_text(
            data['block_message'],
            reply_to_message_id=message.id
        )
        return

    await message.reply_text(
        data['idtext'].format(
            user_id=user_id,
            chat_id=chat_id,
            username=username
        ),
        reply_to_message_id=message.id
    )
