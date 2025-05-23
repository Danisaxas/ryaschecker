from _date import *
from pyrogram import Client, types
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.BoutnAll import es as botones_es
from Source_pack.BoutnAll import en as botones_en
from classBot.MongoDB import MondB
import re

@AstroButton("^re_gen$")
async def regenerate_cards(client: Client, callback_query: types.CallbackQuery):
    reply_msg_id = None
    try:
        user_id = callback_query.from_user.id
        message = callback_query.message
        text = message.text or message.caption or ""
        reply_msg_id = message.reply_to_message.id if message.reply_to_message else message.id
        user_data = MondB(idchat=user_id).queryUser()
        lang = user_data.get("lang", "es")
        ban_status = user_data.get("ban", "No")
        razon = user_data.get("razon", "")
        if lang == "es":
            text_dict = text_es
            botones_dict = botones_es
        elif lang == "en":
            text_dict = text_en
            botones_dict = botones_en
        else:
            text_dict = text_es
            botones_dict = botones_es
        if ban_status == "Yes":
            await callback_query.message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=reply_msg_id
            )
            return
        match = re.search(r"-(.+?)\|([\dx]{2})\|([\dx]{2,4})\|(\w+)-", text)
        if match:
            cc = match.group(1)
            mes = match.group(2)
            ano = match.group(3)
            cvv = match.group(4)
        else:
            await callback_query.message.reply_text(
                "⚠️ Error al regenerar. Asegúrate de que el formato del BIN y los datos sean correctos.",
                reply_to_message_id=reply_msg_id
            )
            return
        mes = "x" if mes.lower() == "xx" else mes
        ano = "x" if ano.lower() == "xx" else ano
        cvv = "x" if cvv.lower() == "rnd" else cvv
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await callback_query.message.reply_text(
                "No se pudieron generar tarjetas válidas con el BIN proporcionado.",
                reply_to_message_id=reply_msg_id
            )
            return
        cards_output = "\n".join(f"<code>{c.strip()}</code>" for c in ccs if c.strip())
        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = (
                f"<code>{bin_info.get('bank_name')}</code> | "
                f"<code>{bin_info.get('vendor')}</code> | "
                f"<code>{bin_info.get('type')}</code> | "
                f"<code>{bin_info.get('level')}</code> | "
                f"<code>{bin_info.get('country')}</code> ({bin_info.get('flag')})"
            )
        else:
            bin_text = "Información no disponible"
        mes_display = mes if mes.lower() not in ["rnd", "x"] else "xx"
        ano_display = ano if ano.lower() not in ["rnd", "x"] else "xx"
        cvv_display = "rnd"
        await callback_query.message.edit_text(
            text_dict['gen_message'].format(
                cc_first6=cc,
                mes_display=mes_display,
                ano_display=ano_display,
                cvv_display=cvv_display,
                cards_output=cards_output,
                bin_text=bin_text,
                bin_first6=cc[:6]
            ),
            reply_markup=botones_dict['re_genbt']
        )
    except Exception as e:
        await callback_query.message.reply_text(
            f"⚠️ Ocurrió un error: {e}",
            reply_to_message_id=reply_msg_id if reply_msg_id else None
        )