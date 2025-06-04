from _date import *
from pyrogram.client import Client
from pyrogram import types
from classBot.MongoDB import MondB
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")
owner_id = 8150119370

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("setpriv")
async def set_priv(client: Client, message: types.Message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()
    admin_lang = (user_data.get("lang") if user_data else "es") or "es"
    admin_lang = admin_lang.lower()

    lang_data = load_language_data(admin_lang)
    if not lang_data:
        lang_data = load_language_data("es")

    if not user_data or user_id != owner_id:
        await message.reply_text(
            lang_data['not_privilegios'],
            reply_to_message_id=message.id
        )
        return

    args = message.text.split()
    if len(args) != 3:
        await message.reply_text(
            lang_data['setpriv_usage'],
            reply_to_message_id=message.id
        )
        return

    _, target_user_id_str, privilegio_str = args
    try:
        target_user_id = int(target_user_id_str.strip())
        privilegio = int(privilegio_str.strip())
    except ValueError:
        await message.reply_text(
            lang_data['setpriv_value_error'],
            reply_to_message_id=message.id
        )
        return

    target_data = MondB(idchat=target_user_id).queryUser()
    if target_data:
        MondB()._client['bot']['user'].update_one(
            {"id": target_user_id},
            {"$set": {"privilegio": privilegio}}
        )
        target_lang = (target_data.get("lang") or "es").lower()
        target_lang_data = load_language_data(target_lang)
        if not target_lang_data:
            target_lang_data = load_language_data("es")

        await message.reply_text(
            target_lang_data['setpriv_success'].format(user_id=target_user_id),
            reply_to_message_id=message.id
        )
    else:
        await message.reply_text(
            lang_data['setpriv_not_found'],
            reply_to_message_id=message.id
        )