from configs.def_main import *
from func_bin import get_bin_info
from func_gen import cc_gen
from pyrogram import Client, filters, types
import random

@ryas("gen")
async def gen(client: Client, message: types.Message):
    """
    Ag-generate iti fake a numero ti credit card base iti naited a BIN.

    Usar: .gen <BIN> [MM] [YYYY] [CVV]
    Ehemplo:
        .gen 426807
        .gen 426807 12 2025
        .gen 426807 12 2025 123
    """
    try:
        input_args = message.text.split()[1:]

        if not input_args:
            await message.reply_text("Usaren: .gen <BIN> [MM] [AAAA] [CVV]", quote=True)
            return

        if len(input_args) < 1:
            await message.reply_text("Nasken nga mangtedka iti saan a basbassit ngem ti BIN.", quote=True)
            return

        cc = input_args[0]
        mes = 'x' if len(input_args) < 2 else input_args[1][0:2]
        ano = 'x' if len(input_args) < 3 else input_args[2]
        cvv = 'x' if len(input_args) < 4 else input_args[3]

        if len(input_args[0]) < 6:
            await message.reply_text("<b>❌ Invalid Bin ❌</b>", quote=True)
            return

        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await message.reply_text("Saan a nakapag-generate kadagiti balido a kard nga addaan iti naited a BIN.", quote=True)
            return

        cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = ccs

        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = f"{bin_info.get('bank_name')} | {bin_info.get('vendor')} | {bin_info.get('type')} | {bin_info.get('level')} | {bin_info.get('country')} ({bin_info.get('flag')})"
        else:
            bin_text = "Saan a magun-od ti impormasion"

        output_message = f"""
[⌥] Onyx Generator | Luhn Algo:
━━━━━━━━━━━━━━
-{cc[:6]}|{mes if mes != 'x' else 'xx'}|{ano if ano != 'x' else 'xx'}|{cvv if cvv != 'x' else 'rnd'}-
━━━━━━━━━━━━━━
{cc1}{cc2}{cc3}{cc4}{cc5}{cc6}{cc7}{cc8}{cc9}{cc10}
━━━━━━━━━━━━━━
[ϟ] Bin : {cc[:6]}  |  [ϟ] Info:
{bin_text}
━━━━━━━━━━━━━━
bot by : @astrozdev🌤
"""
        await message.reply_text(output_message, quote=True)

    except Exception as e:
        await message.reply_text(f"Adda nagdakes a napasamak: {e}", quote=True)
        return
