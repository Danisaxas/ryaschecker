from _date import *
from pyrogram.client import Client
from pyrogram import types
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en

@Astro("setpriv")
async def set_priv(client: Client, message: types.Message):
    owner_id = int(8150119370)
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()
    if not user_data or user_id != owner_id:
        admin_lang = user_data.get("lang", "es") if user_data else 'es'
        text_dict = text_es if admin_lang == 'es' else text_en
        await message.reply_text(text_dict['not_privilegios'], reply_to_message_id=message.id)
        return
    args = message.text.split(" ")
    if len(args) != 3:
        admin_lang = user_data.get("lang", "es") if user_data else 'es'
        text_dict = text_es if admin_lang == 'es' else text_en
        usage_text = "Uso correcto: /setpriv <ID> <Privilegio>" if admin_lang == 'es' else "Correct usage: /setpriv <ID> <Privilege>"
        await message.reply_text(usage_text, reply_to_message_id=message.id)
        return
    _, target_user_id, privilegio = args
    try:
        target_user_id = int(target_user_id.strip())
        privilegio = int(privilegio.strip())
    except ValueError:
        admin_lang = user_data.get("lang", "es") if user_data else 'es'
        text_dict = text_es if admin_lang == 'es' else text_en
        number_error = "El ID y el privilegio deben ser números." if admin_lang == 'es' else "ID and privilege must be numbers."
        await message.reply_text(number_error, reply_to_message_id=message.id)
        return
    target_data = MondB(idchat=target_user_id).queryUser()
    if target_data:
        MondB()._client['bot']['user'].update_one(
            {"id": target_user_id},
            {"$set": {"privilegio": privilegio}}
        )
        target_lang = target_data.get("lang", "es")
        text_dict = text_es if target_lang == 'es' else text_en
        await message.reply_text(
            text_dict['setpriv_success'].format(user_id=target_user_id),
            reply_to_message_id=message.id
        )
    else:
        admin_lang = user_data.get("lang", "es") if user_data else 'es'
        text_dict = text_es if admin_lang == 'es' else text_en
        await message.reply_text(
            text_dict['setpriv_not_found'],
            reply_to_message_id=message.id
        )