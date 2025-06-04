from _date import *
from classBot.MongoDB import MondB
from pyrogram.client import Client
from pyrogram import types
import re
import asyncio
import json
import os

BASE_LOCALES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Locales")

def load_language_data(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_buttons(lang_code: str) -> dict:
    path = os.path.join(BASE_LOCALES_PATH, "button_layouts", f"{lang_code}.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@Astro("gen")
async def gen(client: Client, message: types.Message):
    try:
        user_id = message.from_user.id
        user_data = MondB(idchat=user_id).queryUser()

        lang = (user_data.get('lang') if user_data else 'es') or 'es'
        lang = lang.lower()

        lang_data = load_language_data(lang)
        if not lang_data:
            lang_data = load_language_data("es")

        botones_data = load_buttons(lang)
        if not botones_data:
            botones_data = load_buttons("es")

        ban_status = (user_data.get('status') if user_data else 'Libre') or 'Libre'
        razon = user_data.get('razon', '') if user_data else ''

        entrada = message.text.split(" ", 1)
        if len(entrada) < 2:
            await message.reply_text(lang_data['gen_usage'], quote=True, reply_markup=botones_data.get('gen_but'))
            return

        data = entrada[1].strip()
        if "|" in data:
            parametros = data.split("|")
        else:
            parametros = re.split(r"[ \/:]+", data)

        cc = parametros[0] if len(parametros) >= 1 else ''
        mes = "x"
        ano = "x"
        cvv = "x"

        if len(parametros) >= 2 and parametros[1].strip():
            date_param = parametros[1].strip()
            parts = re.split(r"[\/|:]+", date_param)
            if parts and parts[0].strip():
                mes = parts[0].strip().zfill(2)
            else:
                mes = "x"
            if len(parts) > 1 and parts[1].strip():
                ano = parts[1].strip()
                if len(ano) == 2:
                    ano = "20" + ano
            else:
                ano = "x"

        if len(parametros) >= 3 and not re.search(r"[\/|:]+", parametros[1]) and parametros[2].strip():
            ano = parametros[2].strip()
            if len(ano) == 2:
                ano = "20" + ano

        if len(parametros) >= 4 and parametros[3].strip():
            cvv = parametros[3].strip()

        if len(cc) < 6:
            await message.reply_text(lang_data.get("invalid_bin", "<b>❌ BIN inválido ❌</b>"), quote=True)
            return

        if mes.lower() != "rnd" and mes != "x":
            mes = mes[0:2]

        if ano.lower() != "rnd" and ano != "x":
            if len(ano) == 2:
                ano = "20" + ano

        if cvv.lower() == "rnd" or cvv == "x" or len(parametros) < 3:
            cvv = "x"

        if ban_status.lower() == 'yes':
            await message.reply_text(lang_data['block_message'].format(user_id=user_id, razon=razon), reply_to_message_id=message.id)
            return

        carga = await message.reply_text(lang_data['gen_loading'], quote=True)
        await asyncio.sleep(1)

        ccs = cc_gen(cc, mes, ano, cvv)  # cc_gen debe estar definido en tu proyecto

        if not ccs:
            await carga.edit_text(lang_data.get("no_valid_cards", "No se pudieron generar tarjetas válidas con el BIN proporcionado."))
            return

        cards_output = "\n".join(f"<code>{c.strip()}</code>" for c in ccs if c.strip())

        bin_info = get_bin_info(cc[:6])  # get_bin_info debe estar definido en tu proyecto
        if bin_info:
            bin_text = f"<code>{bin_info.get('bank_name')}</code> | <code>{bin_info.get('vendor')}</code> | <code>{bin_info.get('type')}</code> | <code>{bin_info.get('level')}</code> | <code>{bin_info.get('country')}</code> ({bin_info.get('flag')})"
        else:
            bin_text = lang_data.get("info_no_disponible", "Información no disponible")

        cc_show = cc
        mes_display = mes if mes.lower() not in ["rnd", "x"] else "xx"
        ano_display = ano if ano.lower() not in ["rnd", "x"] else "xx"
        cvv_display = "rnd"
        bin_first6 = cc[:6]

        await carga.edit_text(
            lang_data['gen_message'].format(
                cc_first6=cc_show,
                mes_display=mes_display,
                ano_display=ano_display,
                cvv_display=cvv_display,
                cards_output=cards_output,
                bin_text=bin_text,
                bin_first6=bin_first6
            ),
            reply_markup=botones_data.get('re_genbt')
        )
    except Exception as e:
        await message.reply_text(f"Ocurrió un error: {e}", quote=True)