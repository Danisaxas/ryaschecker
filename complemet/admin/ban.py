from _date import *
from pyrogram.client import Client
from pyrogram import types
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en

@Astro("ban")
async def ban_user(client: Client, message: types.Message):
    try:
        admin_id = message.from_user.id
        admin_username = message.from_user.username or "Usuario"
        admin_data = MondB(idchat=admin_id).queryUser()
        if not admin_data:
            admin_lang = 'es'
            text_dict = text_es
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return

        db = MondB()
        rangos_col = db._db['rangos']
        admin_role = admin_data.get("role", "User")
        rango_doc = rangos_col.find_one({"Rango": {"$regex": f"^{admin_role}$", "$options": "i"}})
        if not rango_doc:
            admin_lang = admin_data.get("lang", "es")
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return
        numero_rango = rango_doc.get("Numero", 0)
        if numero_rango < 3 or numero_rango > 6:
            admin_lang = admin_data.get("lang", "es")
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return

        args = message.text.split(" ", 2)
        if len(args) < 2:
            admin_lang = admin_data.get("lang", "es")
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['ban_usage'], reply_to_message_id=message.id)
            return

        target_identifier = args[1]

        target_user_data = None
        try:
            target_id = int(target_identifier)
            target_user_data = MondB(idchat=target_id).queryUser()
        except ValueError:
            # Buscar por username
            _collection = db._db['user']
            target_user_data = _collection.find_one({"username": target_identifier.lstrip("@")})

        if not target_user_data:
            admin_lang = admin_data.get("lang", "es")
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['ban_validation'], reply_to_message_id=message.id)
            return

        current_status = target_user_data.get("status", "Libre")
        if current_status.lower() == "baneado":
            admin_lang = admin_data.get("lang", "es")
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(
                "<b>El usuario ya está baneado.</b>" if admin_lang == 'en' else "<b>El usuario ya está baneado.</b>",
                reply_to_message_id=message.id
            )
            return

        # Actualizar solo el status a 'Baneado' sin razón
        _id = target_user_data.get("_id")
        db._client['bot']['user'].update_one(
            {"_id": _id},
            {"$set": {"status": "Baneado"}}
        )

        target_username = target_user_data.get("username", "Desconocido")
        target_lang = target_user_data.get("lang", "es")
        text_dict = text_es if target_lang == 'es' else text_en
        ban_message = text_dict['ban_message'].format(
            username=target_username,
            target_user_id=_id,
            ban_reason="No especificada",
            admin_username=admin_username,
            admin_id=admin_id
        )
        await message.reply_text(ban_message, reply_to_message_id=message.id)
    except Exception as e:
        print(f"Error al banear usuario: {e}")
        await message.reply_text(f"Ocurrió un error al banear al usuario: {e}", reply_to_message_id=message.id)
