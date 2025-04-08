from configs.def_main import *
from func_bin import get_bin_info
from func_gen import cc_gen
from pyrogram import Client, filters, types
import random
from datetime import datetime

@ryas("gen")
async def gen(client: Client, message: types.Message):
    """
    Genera números de tarjeta de crédito falsos basados en el BIN proporcionado.

    Uso: .gen <BIN> [MM] [AAAA] [CVV]
    Ejemplos:
        .gen 426807
        .gen 426807 12 2025
        .gen 426807 12 2025 123
        .gen 533516140120xxxx|12|2027|rnd
    """
    try:
        # Extraer el texto posterior al comando (se ignora ".gen")
        entrada = message.text.split(" ", 1)
        if len(entrada) < 2:
            await message.reply_text("Usa: .gen <BIN> [MM] [AAAA] [CVV]", quote=True)
            return

        data = entrada[1]

        # Detectar si se usa "|" o espacios como separador
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
            mes = parametros[1]
        elif len(parametros) == 3:
            mes = parametros[1]
            ano = parametros[2]
        elif len(parametros) >= 4:
            mes = parametros[1]
            ano = parametros[2]
            cvv = parametros[3]

        # Validar que se haya ingresado un BIN con al menos 6 dígitos
        if len(cc) < 6:
            await message.reply_text("<b>❌ Invalid Bin ❌</b>", quote=True)
            return

        # Llamar a cc_gen pasándole todos los parámetros. Si se indican valores "rnd" o "x",
        # la función cc_gen se encargará de generar valores aleatorios para cada tarjeta.
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", quote=True)
            return

        cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = ccs

        # Obtener información del BIN
        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = f"{bin_info.get('bank_name')} | {bin_info.get('vendor')} | {bin_info.get('type')} | {bin_info.get('level')} | {bin_info.get('country')} ({bin_info.get('flag')})"
        else:
            bin_text = "Información no disponible"

        output_message = f"""
[⌥] Onyx Generator | Luhn Algo:
━━━━━━━━━━━━━━
-{cc[:6]}|{mes if mes.lower() != 'rnd' and mes != 'x' else mes}|{ano if ano.lower() != 'rnd' and ano != 'x' else ano}|{cvv if cvv.lower() != 'rnd' and cvv != 'x' else cvv}-
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
