from _date import *
from pyrogram import Client, types
from classBot.MongoDB import MondB
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from datetime import datetime

@Astro('register')
async def register_user(client: Client, message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
    lang = message.from_user.language_code or "es"
    lang = 'en' if lang.startswith("en") else "es"
    try:
        db = MondB(id=user_id, username=username, name=full_name, idchat=user_id)
        if db.queryUser():
            text_dict = text_en if lang == 'en' else text_es
            await message.reply_text(text_dict['already_registered'].format(user=username), reply_to_message_id=message.id)
            return
        db.savedbuser()
        text_dict = text_en if lang == 'en' else text_es
        registro_msg = text_dict['registerx'].format(username=username, user_id=user_id, lang=lang.upper())
        await message.reply_text(registro_msg, reply_to_message_id=message.id)
    except Exception as e:
        print(f"Error en register_user: {e}")
