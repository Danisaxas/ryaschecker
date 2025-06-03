from _date import *
from pyrogram import Client, types
from Source_pack.TextAll import (
    es as text_es,
    en as text_en,
    pt as text_pt,
    ru as text_ru,
    zh as text_zh,
    ko as text_ko,
    fr as text_fr,
    es_mx as text_es_mx,
    tr as text_tr,
    ar as text_ar,
    de as text_de,
    ja as text_ja,
)
from Source_pack.BoutnAll import (
    es as botones_es,
    en as botones_en,
    pt as botones_pt,
    ru as botones_ru,
    zh as botones_zh,
    ko as botones_ko,
    fr as botones_fr,
    es_mx as botones_es_mx,
    tr as botones_tr,
    ar as botones_ar,
    de as botones_de,
    ja as botones_ja,
)
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
        lang = user_data.get("lang", "es").lower()
        ban_status = user_data.get("ban", "No")
        razon = user_data.get("razon", "")

        valid_langs = {"es", "en", "pt", "ru", "zh", "ko", "fr", "es_mx", "tr", "ar", "de", "ja"}
        if lang not in valid_langs:
            lang = "es"

        text_dicts = {
            "es": text_es,
            "en": text_en,
            "pt": text_pt,
            "ru": text_ru,
            "zh": text_zh,
            "ko": text_ko,
            "fr": text_fr,
            "es_mx": text_es_mx,
            "tr": text_tr,
            "ar": text_ar,
            "de": text_de,
            "ja": text_ja,
        }
        botones_dicts = {
            "es": botones_es,
            "en": botones_en,
            "pt": botones_pt,
            "ru": botones_ru,
            "zh": botones_zh,
            "ko": botones_ko,
            "fr": botones_fr,
            "es_mx": botones_es_mx,
            "tr": botones_tr,
            "ar": botones_ar,
            "de": botones_de,
            "ja": botones_ja,
        }

        text_dict = text_dicts[lang]
        botones_dict = botones_dicts[lang]

        if ban_status == "Yes":
            await callback_query.message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=reply_msg_id
            )
            return

        match = re.search(r"-(.+?)\|([\dx]{2})\|([\dx]{2,4})\|(\w+)-", text)
        if not match:
            await callback_query.message.reply_text(
                text_dict.get('re_gen_error', "⚠️ Error al regenerar. Asegúrate de que el formato del BIN y los datos sean correctos."),
                reply_to_message_id=reply_msg_id
            )
            return

        cc, mes, ano, cvv = match.group(1), match.group(2), match.group(3), match.group(4)
        mes = "x" if mes.lower() == "xx" else mes
        ano = "x" if ano.lower() == "xx" else ano
        cvv = "x" if cvv.lower() == "rnd" else cvv

        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await callback_query.message.reply_text(
                text_dict.get('gen_fail', "No se pudieron generar tarjetas válidas con el BIN proporcionado."),
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
            bin_text = text_dict.get('info_unavailable', "Información no disponible")

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
            reply_to_message_id=reply_msg_id
        )