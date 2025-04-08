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
        # Extraer el texto posterior al comando (omitimos ".gen")
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

        # Asignación de parámetros con valores por defecto
        cc = parametros[0] if len(parametros) >= 1 else ''
        mes = 'x'
        ano = 'x'
        cvv = 'x'

        if len(parametros) == 2:
            # Si hay 2 argumentos, asumimos que es BIN y (mes o mes|año)
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

        # --- Procesar valores "rnd" para la fecha y el cvv ---

        # Procesar mes: si se escribió "rnd" se genera un mes aleatorio válido (01 a 12)
        if mes.lower() == "rnd":
            mes = f"{random.randint(1, 12):02d}"
        else:
            # Si se proporcionó el valor manual, asegurarse de tomar solo 2 dígitos
            mes = mes[0:2]

        # Procesar año: si se escribió "rnd" se genera un año aleatorio válido
        if ano.lower() == "rnd":
            current_year = datetime.now().year
            # Se elige un año entre el actual y 5 años en el futuro (puedes ajustar el rango)
            ano = str(random.randint(current_year, current_year + 5))
        # Si se proporciona un año manual se usa el valor tal cual

        # Procesar cvv: si se escribió "rnd" se genera un cvv aleatorio según el tipo de tarjeta
        if cvv.lower() == "rnd":
            # Verificar si es Amex basándonos en el inicio del número (BIN)
            if cc.startswith("34") or cc.startswith("37"):
                # Amex usa cvv de 4 dígitos
                cvv = f"{random.randint(1000, 9999)}"
            else:
                # Otras marcas usan cvv de 3 dígitos
                cvv = f"{random.randint(100, 999)}"
        # Si se ingresó un cvv manual se deja tal cual

        # --- Fin procesamiento rnd ---

        # Generar tarjetas (cc_gen se encarga de aplicar el algoritmo Luhn y demás)
        ccs = cc_gen(cc, mes, ano, cvv)
        if not ccs:
            await message.reply_text("No se pudieron generar tarjetas válidas con el BIN proporcionado.", quote=True)
            return

        cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = ccs

        # Se obtiene la información del BIN
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
