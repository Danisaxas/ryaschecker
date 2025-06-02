from _date import mitad
from classBot.MongoDB import MondB
from pyrogram.types import Message
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es

@Astro("mt")
async def comando_mt(client, message: Message):
    user_id = message.from_user.id
    user = MondB(idchat=user_id).queryUser()

    if not user:
        await message.reply_text(text_es['register_not'], reply_to_message_id=message.id)
        return

    lang = user.get("lang", "es")
    status = user.get("status", "").lower()
    text = text_es if lang == "es" else text_en

    if status == "ban":
        await message.reply_text(
            text['block_message'].format(
                user_id=user_id,
                razon=user.get("razon", "No especificada")
            ),
            reply_to_message_id=message.id
        )
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply_text(text['mt_usage'], reply_to_message_id=message.id)
        return

    try:
        numero = float(args[1])
        resultado = mitad(numero)
        await message.reply_text(
            text['mt_result'].format(numero=numero, resultado=resultado),
            reply_to_message_id=message.id
        )
    except ValueError:
        await message.reply_text(text['mt_invalid'], reply_to_message_id=message.id)
