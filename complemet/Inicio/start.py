from _date import *
import pytz
from datetime import datetime
from pyrogram import Client, types
from classBot.MongoDB import MondB
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from Source_pack.BoutnAll import en as btn_en
from Source_pack.BoutnAll import es as btn_es

@Astro("start")
async def start(client: Client, message: types.Message):
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
        expiracion = user_data.get("expiracion", None)
        lang = user_data.get("lang", "es")
        ban = user_data.get("status", "Libre")
        razon = user_data.get("razon", "No especificada")
        caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")
        if lang == 'es':
            text_dict = text_es
            botones_dict = btn_es
            idioma_actual = "🇪🇸"
        elif lang == 'en':
            text_dict = text_en
            botones_dict = btn_en
            idioma_actual = "🇺🇸"
        else:
            text_dict = text_es
            botones_dict = btn_es
            idioma_actual = "🇪🇸"
        if ban == 'Yes':
            await message.reply_text(text_dict['block_message'].format(user_id=user_id, razon=razon), reply_to_message_id=message.id)
            return
        response = text_dict['startx'].format(username=username, idioma_actual=idioma_actual, caracas_time=caracas_time)
        await message.reply_text(response, reply_to_message_id=message.id, reply_markup=botones_dict['mainstart'])
    except Exception as e:
        print(f"Error en start: {e}")
        await message.reply_text("Ocurrió un error al procesar el comando start.", reply_to_message_id=message.id)
