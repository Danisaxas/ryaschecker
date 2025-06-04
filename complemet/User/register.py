from _date import *
from classBot.MongoDB import MondB
import json
import os

@Astro('register')
async def register_user(client: Client, message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()

    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    data, buttons_data = load_language_file(user_id)

    if user_data:
        await message.reply_text(
            data['already_registered'].format(user=username),
            reply_to_message_id=message.id
        )
        return

    db = MondB(id=user_id, username=username, name=full_name, idchat=user_id)
    db.savedbuser()

    registro_msg = data['registerx'].format(username=username, user_id=user_id, lang=lang.upper())
    await message.reply_text(
        registro_msg,
        reply_to_message_id=message.id
    )
