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
    text_dict = text_es if lang == "es" else text_en

    if str(user_id) != str(owner):
        await message.reply_text(
            "<b>No tienes permisos para usar este comando.</b>",
            reply_to_message_id=message.id
        )
        return

    args = message.text.split()
    if len(args) != 3:
        await message.reply_text(
            "<b>Uso correcto: /setrol ID ROL\nEjemplo: /setrol 123456789 Admin</b>",
            reply_to_message_id=message.id
        )
        return

    _, target_id, role = args
    valid_roles = ["Admin", "Mod", "Seller", "Dev", "Hunter"]

    if role not in valid_roles:
        await message.reply_text(
            f"<b>Rol inválido. Roles permitidos: {', '.join(valid_roles)}</b>",
            reply_to_message_id=message.id
        )
        return

    try:
        target_id = int(target_id.strip())
    except ValueError:
        await message.reply_text(
            "<b>El ID debe ser un número.</b>",
            reply_to_message_id=message.id
        )
        return

    target_user = MondB(idchat=target_id).queryUser()
    if not target_user:
        await message.reply_text(
            "<b>Ese ID no está registrado en la base de datos.</b>",
            reply_to_message_id=message.id
        )
        return

    MondB()._client['bot']['user'].update_one(
        {"id": target_id},
        {"$set": {"role": role}}
    )

    await message.reply_text(
        f"<b>✅ Rol actualizado correctamente:\nID: {target_id}\nNuevo Rol: {role}</b>",
        reply_to_message_id=message.id
    )
