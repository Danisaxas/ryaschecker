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
        .gen 533516140120xxxx|rnd|rnd|rnd
    """
    try:
        # Extraer el texto posterior al comando (se ignora ".gen")
        entrada = message.text.split(" ", 1)
        if len(entrada) < 2:
            await message.reply_text("Usa: .gen <BIN> [MM] [AAAA] [CVV]", quote=True)
            return

        data = entrada[1]

        # Detecta si se usa "|" como separador o si se separa por espacios
        if "|" in data:
            parametros = data.split("|")
        else:
            parametros = data.split()

        # Asignación de parámetros con valores por defecto:
        # Se usa 'x' para indicar que no se proporcionó valor
        cc = parametros[0] if len(parametros) >= 1 else ''
        mes = 'x'
        ano = 'x'
        cvv = 'x'

        if len(parametros) == 2:
            mes = parametros[1]  # Puede ser un valor fijo (ej. "12") o "rnd"
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

        # Si el usuario indicó valores fijos, se procesa:
        # Si el valor es "rnd" se deja sin modificar para que se genere aleatoriamente en cada iteración.
        if mes.lower() != "rnd" and mes != "x":
            mes = mes[0:2]
        if ano.lower() != "rnd" and ano != "x":
            if len(ano) == 2:
                ano = "20" + ano

        # Para cvv, si no es "rnd" ni 'x', se deja el valor como está.

        # Llamar a cc_gen: en ella se generará (por iteración) un valor aleatorio si el campo es "rnd"
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", quote=True)
            return

        cards_output = "".join(ccs)

        # Obtener información del BIN
        bin_info = get_bin_info(cc[:6])
        if bin_info:
            bin_text = (
                f"{bin_info.get('bank_name')} | {bin_info.get('vendor')} | "
                f"{bin_info.get('type')} | {bin_info.get('level')} | "
                f"{bin_info.get('country')} ({bin_info.get('flag')})"
            )
        else:
            bin_text = "Información no disponible"

        output_message = f"""
[⌥] Onyx Generator | Luhn Algo:
━━━━━━━━━━━━━━
-{cc[:6]}|{mes if mes != 'x' else 'xx'}|{ano if ano != 'x' else 'xx'}|{cvv if cvv != 'x' else 'rnd'}-
━━━━━━━━━━━━━━
{cards_output}
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
