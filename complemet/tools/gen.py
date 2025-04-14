from _date import *
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.BoutnAll import es as botones_es
from Source_pack.BoutnAll import en as botones_en
from classBot.MongoDB import MondB
import re
import asyncio

@Astro("gen")
async def gen(client: Client, message: types.Message):
    try:
        user_id = message.from_user.id
        user_data = MondB(idchat=user_id).queryUser()
        if user_data:
            lang = user_data.get('lang', 'es')
            ban_status = user_data.get('status', 'Libre')
            razon = user_data.get('razon', "")
        else:
            lang = 'es'
            ban_status = 'No'
            razon = ""
        if lang == 'es':
            text_dict = text_es
            botones_dict = botones_es
        elif lang == 'en':
            text_dict = text_en
            botones_dict = botones_en
        else:
            text_dict = text_es
            botones_dict = botones_es
        entrada = message.text.split(" ", 1)
        if len(entrada) < 2:
            await message.reply_text(text_dict['gen_usage'], quote=True, reply_markup=botones_dict['gen_but'])
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
            await message.reply_text("<b>❌ Invalid Bin ❌</b>", quote=True)
            return
        if mes.lower() != "rnd" and mes != "x":
            mes = mes[0:2]
        if ano.lower() != "rnd" and ano != "x":
            if len(ano) == 2:
                ano = "20" + ano
        if cvv.lower() == "rnd" or cvv == "x" or len(parametros) < 3:
            cvv = "x"
        user_data = MondB(idchat=user_id).queryUser()
        if user_data:
            lang = user_data.get('lang', 'es')
            ban_status = user_data.get('status', 'Libre')
            razon = user_data.get('razon', "")
        else:
            lang = 'es'
            ban_status = 'No'
            razon = ""
        reply_msg_id = message.reply_to_message.message_id if message.reply_to_message else message.id
        if lang == 'es':
            text_dict = text_es
            botones_dict = botones_es
        elif lang == 'en':
            text_dict = text_en
            botones_dict = botones_en
        else:
            text_dict = text_es
            botones_dict = botones_es
        if ban_status == 'Yes':
            await message.reply_text(text_dict['block_message'].format(user_id=user_id, razon=razon), reply_to_message_id=reply_msg_id)
            return
        carga = await message.reply_text(text_dict['gen_loading'], quote=True)
        await asyncio.sleep(1)
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await carga.edit_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.")
            return
        cards_output = "\n".join(f"<code>{c.strip()}</code>" for c in ccs if c.strip())
        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = f"<code>{bin_info.get('bank_name')}</code> | <code>{bin_info.get('vendor')}</code> | <code>{bin_info.get('type')}</code> | <code>{bin_info.get('level')}</code> | <code>{bin_info.get('country')}</code> ({bin_info.get('flag')})"
        else:
            bin_text = "Información no disponible"
        cc_show = cc
        mes_display = mes if mes.lower() not in ["rnd", "x"] else "xx"
        ano_display = ano if ano.lower() not in ["rnd", "x"] else "xx"
        cvv_display = "rnd"
        bin_first6 = cc[:6]
        await carga.edit_text(text_dict['gen_message'].format(cc_first6=cc_show, mes_display=mes_display, ano_display=ano_display, cvv_display=cvv_display, cards_output=cards_output, bin_text=bin_text, bin_first6=bin_first6), reply_markup=botones_dict['re_genbt'])
    except Exception as e:
        await message.reply_text(f"Ocurrió un error: {e}", quote=True)
        return
