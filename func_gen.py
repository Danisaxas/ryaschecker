import random
from configs.def_main import *

def luhn_verification(num):
    num = [int(d) for d in str(num)]
    check_digit = num.pop()
    num.reverse()
    total = 0
    for i,digit in enumerate(num):
        if i % 2 == 0:
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        total += digit
    total = total * 9
    return (total % 10) == check_digit

def cc_gen(cc, mes='x', ano='x', cvv='x'):
    ccs = []
    while len(ccs) < 10:
        card = str(cc)
        digits = '0123456789'
        list_digits = list(digits)
        random.shuffle(list_digits)
        string_digits = ''.join(list_digits)
        card = card + string_digits
        new_list = list(card)
        list_emty = []

        for i in new_list:
            if i == 'x':
                list_emty.append(str(random.randint(0, 9)))
            else:
                list_emty.append(i)

        list_empty_string = ''.join(list_emty)
        card = list_empty_string

        # Ajustar la longitud de la tarjeta dependiendo del primer dígito
        if card[0] == '3':
            card = card[0:15]
        else:
            card = card[0:16]

        # Generar mes: si se pasó "rnd", se genera un valor aleatorio por iteración
        if mes.lower() == "rnd":
            mes_gen = f"{random.randint(1, 12):02d}"
        elif mes == 'x':
            mes_gen = random.randint(1, 12)
            mes_gen = f"{mes_gen:02d}"
        else:
            mes_gen = mes[0:2]

        # Generar año: si se pasó "rnd", se genera un valor aleatorio por iteración
        if ano.lower() == "rnd":
            # Rango de años: desde el año actual hasta 5 años adelante (puedes ajustar el rango)
            current_year = datetime.now().year
            ano_gen = str(random.randint(current_year, current_year + 5))
        elif ano == 'x':
            ano_gen = random.randint(2023, 2031)
            ano_gen = str(ano_gen)
        else:
            ano_gen = ano
            if len(str(ano_gen)) == 2:
                ano_gen = '20' + str(ano_gen)

        # Generar cvv: si se pasó "rnd", se genera un cvv aleatorio distinto por cada tarjeta
        if cvv.lower() == "rnd":
            if card[0] == '3':  # Puede corresponder a American Express
                cvv_gen = random.randint(1000, 9999)
            else:
                cvv_gen = random.randint(100, 999)
            cvv_gen = str(cvv_gen)
        elif cvv == 'x':
            if card[0] == '3':
                cvv_gen = random.randint(1000, 9999)
            else:
                cvv_gen = random.randint(100, 999)
            cvv_gen = str(cvv_gen)
        else:
            cvv_gen = cvv

        # Genera la tarjeta en el formato deseado
        x = str(card) + '|' + str(mes_gen) + '|' + str(ano_gen) + '|' + str(cvv_gen) + '\n'
        # Verificar con el algoritmo Luhn
        if luhn_verification(card):
            ccs.append(x)
        else:
            continue

    return ccs
