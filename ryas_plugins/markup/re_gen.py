from configs.def_main import *

@ryasbt("^re_gen$")
async def regenerate_cards(client: Client, callback_query: types.CallbackQuery):
    reply_msg_id = None
    try:
        user_id = callback_query.from_user.id
        message = callback_query.message
        text = message.text or message.caption or ""
        reply_msg_id = message.reply_to_message.id if message.reply_to_message else message.id
        connection, cursor = connect_db()
        cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'
        ban_status = result[1] if result else 'No'
        razon = result[2] if result else ""
        chat_id = message.chat.id
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
            await callback_query.message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=reply_msg_id
            )
            return
        match = re.search(r"-(.+?)\|(\d{2})\|(\d{4})\|(\w+)-", text)
        if match:
            cc = match.group(1)
            mes = match.group(2)
            ano = match.group(3)
            cvv = match.group(4)
        else:
            await callback_query.message.reply_text("⚠️ Error al regenerar. Asegúrate de que el formato del BIN y los datos sean correctos.", reply_to_message_id=reply_msg_id)
            return
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await callback_query.message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", reply_to_message_id=reply_msg_id)
            return
        cards_output = "\n".join(f"<code>{c.strip()}</code>" for c in ccs if c.strip())
        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = (
                f"{bin_info.get('bank_name')} | {bin_info.get('vendor')} | "
                f"{bin_info.get('type')} | {bin_info.get('level')} | "
                f"{bin_info.get('country')} ({bin_info.get('flag')})"
            )
        else:
            bin_text = "Información no disponible"
        await callback_query.message.edit_text(
            text_dict['gen_message'].format(
                cc_first6=cc,
                mes_display=mes,
                ano_display=ano,
                cvv_display=cvv,
                cards_output=cards_output,
                bin_text=bin_text,
                bin_first6=cc[:6]
            ),
            reply_markup=botones_dict['re_genbt']
        )
    except Exception as e:
        await callback_query.message.reply_text(f"⚠️ Ocurrió un error: {e}", reply_to_message_id=reply_msg_id if reply_msg_id else None)
