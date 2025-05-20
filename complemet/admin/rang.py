from _date import *
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from classBot.MongoDB import MondB
from pyrogram.client import Client
from pyrogram import types

@Astro("rang")
async def rang_handler(client: Client, message: types.Message):
    user_id = str(message.from_user.id)
    user_lang = message.from_user.language_code or 'es'
    user_lang = 'en' if user_lang.startswith('en') else 'es'
    text_dict = text_en if user_lang == 'en' else text_es

    if user_id != owner:
        await message.reply_text(
            "<b>Access denied. You do not have permission to use this command.</b>" if user_lang == 'en' else "<b>Acceso denegado. No tienes permiso para usar este comando.</b>",
            reply_to_message_id=message.id
        )
        return

    args = message.text.split(maxsplit=4)
    if len(args) < 5:
        usage_msg = "<b>Usage: /rang Numero Rango Priv Obsequiar</b>" if user_lang == 'en' else "<b>Uso: /rang Numero Rango Priv Obsequiar</b>"
        await message.reply_text(usage_msg, reply_to_message_id=message.id)
        return

    _, numero_str, rango, priv, obsequiar = args

    if not numero_str.isdigit():
        error_msg = "<b>Numero must be a number.</b>" if user_lang == 'en' else "<b>El Numero debe ser un número.</b>"
        await message.reply_text(error_msg, reply_to_message_id=message.id)
        return

    numero = int(numero_str)
    obsequiar_list = obsequiar.split(',')

    db = MondB()
    rangos_col = db._db['rangos']

    # Insert or update document with upsert=True
    rangos_col.update_one(
        {"Numero": numero},
        {
            "$set": {
                "Rango": rango,
                "Priv": priv,
                "Obsequiar": obsequiar_list
            }
        },
        upsert=True
    )

    success_msg = f"<b>Rango actualizado:\nNumero: {numero}\nRango: {rango}\nPriv: {priv}\nObsequiar: {', '.join(obsequiar_list)}</b>" if user_lang == 'en' else \
                  f"<b>Rango actualizado:\nNumero: {numero}\nRango: {rango}\nPriv: {priv}\nObsequiar: {', '.join(obsequiar_list)}</b>"

    await message.reply_text(success_msg, reply_to_message_id=message.id)
