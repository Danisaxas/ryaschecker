from _date import *
from pyrogram import Client, types
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en

@Astro("ban")
async def ban_user(client: Client, message: types.Message):
    try:
        admin_id = message.from_user.id
        admin_username = message.from_user.username or "Usuario"
        admin_data = MondB(idchat=admin_id).queryUser()
        if not admin_data or admin_data.get("role", "User") != "Admin":
            admin_lang = admin_data.get("lang", "es") if admin_data else 'es'
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return
        args = message.text.split(" ", 2)
        if len(args) < 2:
            admin_lang = admin_data.get("lang", "es")
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['ban_usage'], reply_to_message_id=message.id)
            return
        target_user_id = args[1]
        ban_reason = args[2] if len(args) > 2 else "No especificada"
        try:
            target_user_id = int(target_user_id)
        except ValueError:
            admin_lang = admin_data.get("lang", "es")
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['ban_validation'], reply_to_message_id=message.id)
            return
        MondB()._client['bot']['user'].update_one(
            {"id": target_user_id},
            {"$set": {"status": "Baneado", "razon": ban_reason}}
        )
        target_user_data = MondB(idchat=target_user_id).queryUser()
        target_username = target_user_data.get("username", "Desconocido")
        target_lang = target_user_data.get("lang", "es")
        text_dict = text_es if target_lang == 'es' else text_en
        ban_message = text_dict['ban_message'].format(
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