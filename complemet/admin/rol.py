from _date import *
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from classBot.MongoDB import MondB, queryUser
from pyrogram.client import Client
from pyrogram import types

@Astro("setrol")
async def set_role(client: Client, message: types.Message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()

    lang = user_data.get("lang", "es") if user_data else "es"
    lang = lang.lower()
    lang = 'en' if lang.startswith('en') else 'es'
    text_dict = text_en if lang == "en" else text_es

    if str(user_id) != str(owner):
        await message.reply_text(
            text_dict['setrol_no_permission'],
            reply_to_message_id=message.id
        )
        return

    args = message.text.split()
    if len(args) != 3:
        await message.reply_text(
            text_dict['setrol_usage'],
            reply_to_message_id=message.id
        )
        return

    _, target_id_str, role_input = args

    try:
        target_id = int(target_id_str.strip())
    except ValueError:
        await message.reply_text(
            text_dict['setrol_not_number'],
            reply_to_message_id=message.id
        )
        return

    db = MondB()
    rangos_col = db._db['rangos']

    if not role_input.isdigit():
        await message.reply_text(
            text_dict['setrol_invalid'],
            reply_to_message_id=message.id
        )
        return

    role_num = int(role_input)
    rango_doc = rangos_col.find_one({"Numero": role_num})
    if not rango_doc:
        await message.reply_text(
            text_dict['setrol_invalid'],
            reply_to_message_id=message.id
        )
        return

    role_name = rango_doc.get("Rango", "").title()

    target_user = queryUser(target_id)
    if not target_user:
        await message.reply_text(
            text_dict['setrol_not_found'],
            reply_to_message_id=message.id
        )
        return

    current_role = target_user.get("role", "User").title()
    if current_role == role_name:
        await message.reply_text(
            text_dict['setrol_already_has'].format(role=role_name),
            reply_to_message_id=message.id
        )
        return

    db._client['bot']['user'].update_one(
        {"_id": target_id},
        {"$set": {"role": role_name}}
    )

    await message.reply_text(
        text_dict['setrol_success'].format(id=target_id, role=role_name),
        reply_to_message_id=message.id
    )
