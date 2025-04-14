from _date import *
from pyrogram import Client, types
from classBot.sql import MondB
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es

@Astro('me')
async def me_command(client: Client, message: types.Message):
    user_id = message.from_user.id
    try:
        username = message.from_user.username or "Usuario"
        full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
        user_lang = message.from_user.language_code or 'es'
        user_lang = 'en' if user_lang.startswith('en') else 'es'
        db = MondB(id=user_id, username=username, name=full_name, idchat=user_id)
        user_data = db.queryUser()
        if not user_data:
            if user_lang == 'en':
                await message.reply_text(text_en['register_not'], reply_to_message_id=message.id)
            else:
                await message.reply_text(text_es['register_not'], reply_to_message_id=message.id)
            return
        rango = user_data.get("plan", "Free User")
        creditos = user_data.get("credits", 0)
        antispam = user_data.get("antispam", 60)
        expiration = user_data.get("expiracion", "No plan contrated")
        lang = user_data.get("lang", "es")
        ban = user_data.get("status", "Libre")
        if lang == 'en':
            text_dict = text_en
        else:
            text_dict = text_es
        formatted_text = text_dict['metext'].format(
            username=username,
            user_id=user_id,
            rango=rango,
            creditos=creditos,
            antispam=antispam,
            expiration=expiration,
            ban=ban
        )
        await message.reply_text(formatted_text, reply_to_message_id=message.id)
    except Exception as e:
        print(f"Error en me_command: {e}")
        await message.reply_text("Ocurrió un error al procesar el comando me.", reply_to_message_id=message.id)
