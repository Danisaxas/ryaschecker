from configs.def_main import *
from func_bin import get_bin_info
from func_gen import cc_gen
from pyrogram import Client, filters, types
import random

@ryas("gen")
async def gen(client: Client, message: types.Message):
    """
    Genera números de tarjeta de crédito falsos basados en el BIN proporcionado.

    Uso: .gen <BIN> [MM] [AAAA] [CVV]
    Ejemplos:
        .gen 426807
        .gen 426807 12 2025
        .gen 426807 12 2025 123
        .gen 463846003763xxxx|03|2028|rnd
    """
    try:
        # Extraer el texto posterior al comando (omitimos ".gen")
        entrada = message.text.split(" ", 1)
        if len(entrada) < 2:
            await message.reply_text("Usa: .gen <BIN> [MM] [AAAA] [CVV]", quote=True)
            return

        data = entrada[1]

        # Verificar si se usa "|" como separador
        if "|" in data:
            parametros = data.split("|")
        else:
            parametros = data.split()

        # Asignación de parámetros con valores por defecto
        cc = parametros[0] if len(parametros) >= 1 else ''
        mes = 'x'
        ano = 'x'
        cvv = 'x'

        if len(parametros) == 2:
            # Se asume que se pasan mes y año juntos (delimitados por "|") o solo mes si se usan espacios.
            mes = parametros[1][0:2]  # En caso de usar espacios, tomamos solo los dos primeros dígitos
            # Si se usó "|" debería venir tanto mes como año
            if "|" in data and len(parametros) >= 2:
                ano = parametros[1] if len(parametros) > 1 else 'x'
        elif len(parametros) == 3:
            mes = parametros[1][0:2]
            ano = parametros[2]
        elif len(parametros) >= 4:
            mes = parametros[1][0:2]
            ano = parametros[2]
            cvv = parametros[3]

        # Validación del BIN
        if len(cc) < 6:
            await message.reply_text("<b>❌ Invalid Bin ❌</b>", quote=True)
            return

        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", quote=True)
            return

        cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = ccs

        bin_info = get_bin_info(cc[:6])
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
