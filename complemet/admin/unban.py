from _date import *
from pyrogram.client import Client
from pyrogram import types
from classBot.MongoDB import MondB
from datetime import datetime
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("unban")
async def unban_user(client: Client, message: types.Message):
    try:
        admin_id = message.from_user.id
        admin_username = message.from_user.username or "Usuario"

        admin_data = MondB(idchat=admin_id).queryUser()
        admin_lang = (admin_data.get("lang") if admin_data else "es") or "es"
        admin_lang = admin_lang.lower()

        lang_data = load_language_data(admin_lang)
        if not lang_data:
            lang_data = load_language_data("es")

        if not admin_data:
            await message.reply_text(lang_data['not_privilegios'], reply_to_message_id=message.id)
            return

        db = MondB()
        rangos_col = db._db['rangos']
        admin_role = admin_data.get("role", "User")
        rango_doc = rangos_col.find_one({"Rango": {"$regex": f"^{admin_role}$", "$options": "i"}})
        if not rango_doc:
            await message.reply_text(lang_data['not_privilegios'], reply_to_message_id=message.id)
            return

        numero_rango = rango_doc.get("Numero", 0)
        if numero_rango < 3 or numero_rango > 6:
            await message.reply_text(lang_data['not_privilegios'], reply_to_message_id=message.id)
            return

        args = message.text.split()
        if len(args) != 2:
            await message.reply_text(lang_data['unban_usage'], reply_to_message_id=message.id)
            return

        target_identifier = args[1]

        target_user_data = None
        try:
            target_id = int(target_identifier)
            target_user_data = MondB(idchat=target_id).queryUser()
        except ValueError:
            _collection = db._db['user']
            target_user_data = _collection.find_one({"username": target_identifier.lstrip("@")})

        if not target_user_data:
            await message.reply_text(lang_data['unban_validation'], reply_to_message_id=message.id)
            return

        current_status = target_user_data.get("status", "Libre")
        if current_status.lower() != "baneado":
            await message.reply_text(lang_data.get('not_banned', "<b>El usuario no está baneado.</b>"), reply_to_message_id=message.id)
            return

        _id = target_user_data.get("_id")
        db._client['bot']['user'].update_one(
            {"_id": _id},
            {"$set": {"status": "Libre"}}
        )

        target_username = target_user_data.get("username", "Desconocido")
        target_lang = (target_user_data.get("lang") or "es").lower()
        target_lang_data = load_language_data(target_lang)
        if not target_lang_data:
            target_lang_data = load_language_data("es")

        unban_message = target_lang_data['unban_message'].format(
            username=target_username,
            target_user_id=_id,
            fecha=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            admin_username=admin_username,
            admin_id=admin_id
        )
        await message.reply_text(unban_message, reply_to_message_id=message.id)

    except Exception as e:
        print(f"Error inesperado: {e}")
        await message.reply_text(f"Ocurrió un error inesperado: {e}", reply_to_message_id=message.id)