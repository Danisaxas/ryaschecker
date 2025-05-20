from _date import *
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from classBot.MongoDB import MondB
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

    _, target_id, role_input = args
    role_clean = role_input.title()

    valid_roles = ["Admin", "Mod", "Seller", "Dev", "Hunter"]
    if role_clean not in valid_roles:
        await message.reply_text(
            text_dict['setrol_invalid'],
            reply_to_message_id=message.id
        )
        return

    try:
        target_id = int(target_id.strip())
    except ValueError:
        await message.reply_text(
            text_dict['setrol_not_number'],
            reply_to_message_id=message.id
        )
        return

    target_user = MondB(idchat=target_id).queryUser()
    if not target_user:
        await message.reply_text(
            text_dict['setrol_not_found'],
            reply_to_message_id=message.id
        )
        return

    current_role = target_user.get("role", "User").title()
    if current_role == role_clean:
        await message.reply_text(
            text_dict['setrol_already_has'].format(role=role_input),
            reply_to_message_id=message.id
        )
        return

    MondB()._client['bot']['user'].update_one(
        {"_id": target_id},
        {"$set": {"role": role_clean}}
    )

    await message.reply_text(
        text_dict['setrol_success'].format(id=target_id, role=role_input),
        reply_to_message_id=message.id
    )