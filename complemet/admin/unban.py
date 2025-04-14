from _date import *
from pyrogram import Client, types
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en

@Astro("unban")
async def unban_user(client: Client, message: types.Message):
    connection = None
    cursor = None
    try:
        admin_id = message.from_user.id
        admin_username = message.from_user.username or "Usuario"

        db = MondB()
        connection, cursor = db.connect()
        cursor.execute("SELECT privilegio, lang FROM users WHERE user_id = %s", (admin_id,))
        admin_data = cursor.fetchone()
        if not admin_data or admin_data[0] < 3:
            admin_lang = admin_data[1] if admin_data else 'es'
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
            return
        args = message.text.split()
        if len(args) != 2:
            admin_lang = admin_data[1] if admin_data else 'es'
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['unban_usage'], reply_to_message_id=message.id)
            return
        target_user_id = args[1]
        try:
            target_user_id = int(target_user_id)
        except ValueError:
            admin_lang = admin_data[1] if admin_data else 'es'
            text_dict = text_es if admin_lang == 'es' else text_en
            await message.reply_text(text_dict['unban_validation'], reply_to_message_id=message.id)
            return
        target_data = MondB(idchat=target_user_id).queryUser()
        if target_data:
            MondB()._client['bot']['user'].update_one(
                {"user_id": target_user_id},
                {"$set": {"ban": 'No', "razon": None}},
                upsert=True
            )
            target_username = message.from_user.username or "Desconocido"
            target_lang = admin_data[1] if admin_data else 'es'
            text_dict = text_es if target_lang == 'es' else text_en
            unban_message = text_dict['unban_message'].format(
                username=target_username,
                target_user_id=target_user_id,
                fecha=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                admin_username=admin_username,
                admin_id=admin_id
            )
            await message.reply_text(unban_message, reply_to_message_id=message.id)
    except Exception as e:
        print(f"Error inesperado: {e}")
        await message.reply_text(f"Ocurrió un error inesperado: {e}", reply_to_message_id=message.id)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()