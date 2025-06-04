from _date import *
from pyrogram.client import Client
from pyrogram import types
from classBot.MongoDB import MondB
import json
import os

@Astro("ban")
async def ban_user(client: Client, message: types.Message):
    try:
        admin_id = message.from_user.id
        admin_username = message.from_user.username or "Usuario"

        admin_data = MondB(idchat=admin_id).queryUser()
        admin_lang = (admin_data.get("lang") if admin_data else "es") or "es"
        admin_lang = admin_lang.lower()

        data, buttons_data = load_language_file(admin_id)

        if not admin_data:
            await message.reply_text(data['not_privilegios'], reply_to_message_id=message.id)
            return

        db = MondB()
        rangos_col = db._db['rangos']
        admin_role = admin_data.get("role", "User")
        rango_doc = rangos_col.find_one({"Rango": {"$regex": f"^{admin_role}$", "$options": "i"}})
        if not rango_doc:
            await message.reply_text(data['not_privilegios'], reply_to_message_id=message.id)
            return

        numero_rango = rango_doc.get("Numero", 0)
        if numero_rango < 3 or numero_rango > 6:
            await message.reply_text(data['not_privilegios'], reply_to_message_id=message.id)
            return

        args = message.text.split(" ", 2)
        if len(args) < 2:
            await message.reply_text(data['ban_usage'], reply_to_message_id=message.id)
            return

        target_user_id = args[1]
        ban_reason = args[2] if len(args) > 2 else "No especificada"
        try:
            target_user_id = int(target_user_id)
        except ValueError:
            await message.reply_text(data['ban_validation'], reply_to_message_id=message.id)
            return

        target_user_data = MondB(idchat=target_user_id).queryUser()
        if not target_user_data:
            await message.reply_text(data['ban_validation'], reply_to_message_id=message.id)
            return

        current_status = target_user_data.get("status", "Libre")
        if current_status.lower() == "baneado":
            await message.reply_text(data.get('already_banned', "<b>El usuario ya está baneado.</b>"), reply_to_message_id=message.id)
            return

        MondB()._client['bot']['user'].update_one(
            {"_id": target_user_id},
            {"$set": {"status": "Baneado", "razon": ban_reason}}
        )

        target_username = target_user_data.get("username", "Desconocido")
        target_lang = (target_user_data.get("lang") or "es").lower()
        target_lang_data = load_language_file(target_user_id)[0]
        if not target_lang_data:
            target_lang_data = load_language_file("es")[0]

        ban_message = target_lang_data['ban_message'].format(
            username=target_username,
            target_user_id=target_user_id,
            ban_reason=ban_reason,
            admin_username=admin_username,
            admin_id=admin_id
        )
        await message.reply_text(ban_message, reply_to_message_id=message.id)
    except Exception as e:
        print(f"Error al banear usuario: {e}")
        await message.reply_text(f"Ocurrió un error al banear al usuario: {e}", reply_to_message_id=message.id)
