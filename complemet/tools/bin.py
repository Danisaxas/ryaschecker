from pyrogram import Client, types
from classBot.MongoDB import MondB
from _date import *
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_bin_info(bin_number: str) -> dict:
    # Implementa aquí la lógica para obtener información real del BIN
    # Este es un ejemplo de placeholder
    dummy_data = {
        "flag": "🇺🇸",
        "bank_name": "Bank Example",
        "vendor": "Visa",
        "type": "Credit",
        "level": "Platinum",
        "country": "United States",
        "iso": "US"
    }
    if len(bin_number) == 6 and bin_number.isdigit():
        return dummy_data
    return None

@Astro("bin")
async def bin_command(client: Client, message: types.Message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()

    lang = (user_data.get('lang') if user_data else 'es') or 'es'
    lang = lang.lower()

    lang_data = load_language_data(lang)
    if not lang_data:
        lang_data = load_language_data("es")

    ban_status = (user_data.get('status') if user_data else 'Libre') or 'Libre'
    razon = user_data.get('razon', '') if user_data else ''

    if ban_status.lower() != 'libre':
        await message.reply_text(
            lang_data['block_message'].format(user_id=user_id, razon=razon),
            reply_to_message_id=message.id
        )
        return

    parts = message.text.split()
    if len(parts) < 2:
        await message.reply_text(lang_data['bin_usage'], reply_to_message_id=message.id)
        return

    bin_number = parts[1][:6]
    if not bin_number.isdigit():
        await message.reply_text(lang_data['bin_error'], reply_to_message_id=message.id)
        return

    bin_info = get_bin_info(bin_number)
    if bin_info:
        rango_usuario = user_data.get('role', 'Free User') if user_data else "Free User"
        username = message.from_user.username or message.from_user.first_name or 'Unknown'
        respuesta = lang_data['bintext'].format(
            bandera=bin_info['flag'],
            bin_number=bin_number,
            bank_name=bin_info['bank_name'],
            vendor=bin_info['vendor'],
            type=bin_info['type'],
            level=bin_info['level'],
            pais=bin_info['country'],
            pais_codigo=bin_info['iso'],
            username=username,
            rango=rango_usuario
        )
        await message.reply_text(respuesta, reply_to_message_id=message.id)
    else:
        await message.reply_text(
            lang_data['bin_not_found'].format(bin_number=bin_number),
            reply_to_message_id=message.id
        )