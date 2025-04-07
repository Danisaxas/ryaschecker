from configs.def_main import * # Import the main configuration
from func_bin import get_bin_info  # Import the function to get BIN information
from func_gen import cc_gen  # Import the function to generate credit card numbers
from pyrogram import Client, filters, types  # Import necessary Pyrogram modules
import random

@ryas("gen") # Changed Decorator
async def gen(client: Client, message: types.Message):
    """
    Generates fake credit card numbers based on the provided BIN.

    Usage: .gen <BIN> [MM] [YYYY] [CVV]
    Examples:
        .gen 426807
        .gen 426807 12 2025
        .gen 426807 12 2025 123
    """
    try:
        input_args = message.text.split()[1:]  # Get arguments after the command

        if not input_args:
            await message.reply_text("Usa: .gen <BIN> [MM] [AAAA] [CVV]", quote=True)
            return

        if len(input_args) < 1:
            await message.reply_text("Debes proporcionar al menos el BIN.", quote=True)
            return

        cc = input_args[0]
        mes = 'x' if len(input_args) < 2 else input_args[1][0:2]
        ano = 'x' if len(input_args) < 3 else input_args[2]
        cvv = 'x' if len(input_args) < 4 else input_args[3]

        if len(input_args[0]) < 6:
            await message.reply_text("<b>❌ Invalid Bin ❌</b>", quote=True)
            return

        ccs = cc_gen(cc, mes, ano, cvv)  # Generate the credit card numbers
        if not ccs:
            await message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", quote=True)
            return

        cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = ccs

        bin_info = get_bin_info(cc[:6])  # Get BIN information
        if bin_info:
            bin_text = f"{bin_info.get('bank_name')} | {bin_info.get('vendor')} | {bin_info.get('type')} | {bin_info.get('level')} | {bin_info.get('country')} ({bin_info.get('flag')})"
        else:
            bin_text = "Información no disponible"

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
        await message.reply_text(f"Ocurrió un error: {e}", quote=True)
        return
