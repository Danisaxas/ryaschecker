from _date import *
from classBot.MongoDB import MondB
from pyrogram.client import Client
from pyrogram import types
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("rang")
async def rang_handler(client: Client, message: types.Message):
    user_id = str(message.from_user.id)
    user_lang = message.from_user.language_code or 'es'
    user_lang = 'en' if user_lang.startswith('en') else 'es'

    lang_data = load_language_data(user_lang)
    if not lang_data:
        lang_data = load_language_data("es")

    if int(user_id) != owner:
        await message.reply_text(
            lang_data['not_privilegios'],
            reply_to_message_id=message.id
        )
        return

    args = message.text.split(maxsplit=4)
    if len(args) < 5:
        await message.reply_text(
            lang_data['rang_usage'],
            reply_to_message_id=message.id
        )
        return

    _, numero_str, rango, priv, obsequiar = args

    if not numero_str.isdigit():
        await message.reply_text(
            lang_data['rang_numero_error'],
            reply_to_message_id=message.id
        )
        return

    numero = int(numero_str)
    obsequiar_list = obsequiar.split(',')

    db = MondB()
    rangos_col = db._db['rangos']

    rangos_col.update_one(
        {"Numero": numero},
        {
            "$set": {
                "Rango": rango,
                "Priv": priv,
                "Obsequiar": obsequiar_list
            }
        },
        upsert=True
    )

    await message.reply_text(
        lang_data['rang_success'].format(
            numero=numero,
            rango=rango,
            priv=priv,
            obsequiar=', '.join(obsequiar_list)
        ),
        reply_to_message_id=message.id
    )