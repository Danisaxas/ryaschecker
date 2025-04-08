from configs.def_main import *

@ryas("gen")
async def gen(client: Client, message: types.Message):
    try:
        entrada = message.text.split(" ", 1)
        if len(entrada) < 2:
            await message.reply_text("Usa: .gen <BIN> [MM/AA] [CVV]", quote=True)
            return
        data = entrada[1].strip()
        if "|" in data:
            parametros = data.split("|")
        else:
            parametros = data.split()
        cc = parametros[0] if len(parametros) >= 1 else ''
        mes = "x"
        ano = "x"
        cvv = "x"
        if len(parametros) >= 2 and parametros[1].strip():
            date_param = parametros[1].strip()
            if "/" in date_param:
                parts = date_param.split("/")
                mes = parts[0].strip()
                ano = parts[1].strip()
                if len(ano) == 2:
                    ano = "20" + ano
            else:
                mes = date_param
        if len(parametros) >= 3 and not ("/" in parametros[1]) and parametros[2].strip():
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
        if (len(parametros) < 3 or not ano.strip()) and mes.lower() != "rnd":
            from random import randint
            ano = str(randint(datetime.now().year + 1, datetime.now().year + 5))
        elif ano.lower() != "rnd" and ano != "x":
            if len(ano) == 2:
                ano = "20" + ano
        else:
            ano = "x"
        if cvv.lower() == "rnd" or cvv == "x" or len(parametros) < 4:
            cvv = "x"
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", quote=True)
            return
        cards_output = "\n".join(f"<code>{c.strip()}</code>" for c in ccs if c.strip())
        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = (f"{bin_info.get('bank_name')} | {bin_info.get('vendor')} | "
                        f"{bin_info.get('type')} | {bin_info.get('level')} | "
                        f"{bin_info.get('country')} ({bin_info.get('flag')})")
        else:
            bin_text = "Información no disponible"
        user_id = message.from_user.id
        connection, cursor = connect_db()
        cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'
        ban_status = result[1] if result else 'No'
        razon = result[2] if result else ""
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message.message_id if message.reply_to_message else message.id
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
            from ryas_templates.botones import es as botones_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
            from ryas_templates.botones import en as botones_dict
        else:
            from ryas_templates.chattext import es as text_dict
            from ryas_templates.botones import es as botones_dict
        if ban_status == 'Yes':
            await message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=reply_msg_id
            )
            return
        cc_show = cc
        mes_display = mes if mes.lower() not in ["rnd", "x"] else "xx"
        ano_display = ano if ano.lower() not in ["rnd", "x"] else "xx"
        cvv_display = "rnd"
        bin_first6 = cc[:6]
        await message.reply_text(
            text_dict['gen_message'].format(
                cc_first6=cc_show,
                mes_display=mes_display,
                ano_display=ano_display,
                cvv_display=cvv_display,
                cards_output=cards_output,
                bin_text=bin_text,
                bin_first6=bin_first6
            ),
            reply_to_message_id=reply_msg_id,
            reply_markup=botones_dict['re_genbt']
        )
    except Exception as e:
        await message.reply_text(f"Ocurrió un error: {e}", quote=True)
        return
