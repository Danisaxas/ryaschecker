from configs.def_main import *
from pyrogram.types import CallbackQuery
from func_bin import get_bin_info
from func_gen import cc_gen
from datetime import datetime

@ryasbt("^re_gen$")
async def regen_handler(client, callback_query: CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        connection, cursor = connect_db()
        cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'
        ban_status = result[1] if result else 'No'
        razon = result[2] if result else ""

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
            await callback_query.answer("Estás bloqueado.", show_alert=True)
            return

        original_text = callback_query.message.text or callback_query.message.caption

        # Extraer BIN desde el mensaje original (el que contiene .gen ...)
        import re
        bin_match = re.search(r"BIN:\s*(\d{6,})", original_text)
        mes_match = re.search(r"Fecha:\s*(\d{2})", original_text)
        ano_match = re.search(r"/(\d{2,4})", original_text)
        cvv_match = re.search(r"CVV:\s*(\w+)", original_text)

        cc = bin_match.group(1) if bin_match else None
        mes = mes_match.group(1) if mes_match else "x"
        ano = ano_match.group(1) if ano_match else "x"
        cvv = cvv_match.group(1) if cvv_match else "x"

        # Convertir año corto a largo si es necesario
        if len(ano) == 2:
            ano = "20" + ano

        # Si hay algún campo en "rnd", se convierte en "x" para que se regenere aleatoriamente
        if mes.lower() == "rnd":
            mes = "x"
        if ano.lower() == "rnd":
            ano = "x"
        if cvv.lower() == "rnd":
            cvv = "x"

        # Generar nuevas tarjetas
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await callback_query.answer("❌ Error generando tarjetas", show_alert=True)
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

        mes_display = mes if mes != "x" else "xx"
        ano_display = ano[-2:] if ano != "x" else "xx"
        cvv_display = "rnd"
        bin_first6 = cc[:6]

        await callback_query.message.edit_text(
            text_dict['gen_message'].format(
                cc_first6=cc,
                mes_display=mes_display,
                ano_display=ano_display,
                cvv_display=cvv_display,
                cards_output=cards_output,
                bin_text=bin_text,
                bin_first6=bin_first6
            ),
            reply_markup=botones_dict['re_genbt']
        )

        await callback_query.answer("✅ Tarjetas regeneradas")

    except Exception as e:
        await callback_query.answer("⚠️ Error al regenerar", show_alert=True)
        print("Error en re_gen:", e)
