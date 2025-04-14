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
            await message.reply_text(text_dict['already_registered'].format(user=username))
            return
        db.insertUser({
            "plan": "Free User",
            "privilegio": 0,
            "credits": 0,
            "antispam": 60,
            "expiracion": None,
            "dias": 0,
            "bin_lasted": None,
            "status": "Libre",
            "lang": lang
        })
        text_dict = text_en if lang == 'en' else text_es
        registro_msg = text_dict['registerx'].format(
            username=username, user_id=user_id, lang=lang.upper()
        )
        log_msg = f"""
✅ ¡Nuevo Registro!
━━━━━━━━━━━━━
👤 Usuario: @{username}
🆔 ID: {user_id}
⺢ Fecha: {datetime.now().strftime('%Y-%m-%d')}
🌍 Idioma: {lang}
━━━━━━━━━━━━━
🎯 ¡Bienvenido a RyasChk!
"""
        await message.reply_text(registro_msg)
        await client.send_message(_channel, log_msg)
    except Exception as e:
        print(f"Error en register_user: {e}")
        await message.reply_text(f"Ocurrió un error durante el registro: {e}")