from pyrogram import Client, filters, types
from configs.def_main import *
from func_bin import get_bin_info
from func_gen import cc_gen
from datetime import datetime

@ryasbt("^re_gen$")
async def regenerate_cards(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        message = callback_query.message
        text = message.text or message.caption or ""

        # Obtener idioma y estado del usuario
        connection, cursor = connect_db()
        cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'
        ban_status = result[1] if result else 'No'
        razon = result[2] if result else ""
        chat_id = callback_query.message.chat.id
        reply_msg_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id

        # Selección del idioma y botones
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
            from ryas_templates.botones import es as botones_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict_en
            from ryas_templates.botones import en as botones_dict_en
        else:
            from ryas_templates.chattext import es as text_dict
            from ryas_templates.botones import es as botones_dict

        # Verificar si el usuario está baneado
        if ban_status == 'Yes':
            await callback_query.message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=reply_msg_id
            )
            return

        # Extraer el BIN y los detalles de la tarjeta
        match = re.search(r"(\d{6})\|(\d{2})\|(\d{4})\|([0-9]{3})", text)
        if match:
            cc = match.group(1)
            mes = match.group(2)
            ano = match.group(3)
            cvv = match.group(4)
        else:
            await callback_query.message.reply_text("⚠️ Error al regenerar. Asegúrate de que el formato del BIN y los datos sean correctos.", reply_to_message_id=reply_msg_id)
            return

        # Regenerar las tarjetas
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await callback_query.message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", reply_to_message_id=reply_msg_id)
            return

        # Nuevas tarjetas generadas
        cards_output = "\n".join(f"<code>{c.strip()}</code>" for c in ccs if c.strip())

        # Obtener información adicional del BIN
        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = (
                f"{bin_info.get('bank_name')} | {bin_info.get('vendor')} | "
                f"{bin_info.get('type')} | {bin_info.get('level')} | "
                f"{bin_info.get('country')} ({bin_info.get('flag')})"
            )
        else:
            bin_text = "Información no disponible"

        # Actualizar el mensaje con las nuevas tarjetas y la información
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
            reply_markup=botones_dict['re_genbt'],  # Se mantiene el botón de regenerar
            reply_to_message_id=reply_msg_id
        )

    except Exception as e:
        await callback_query.message.reply_text(f"⚠️ Ocurrió un error: {e}", reply_to_message_id=reply_msg_id)
