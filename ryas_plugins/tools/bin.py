from pyrogram import Client, types  # Importa Client y types de Pyrogram
import requests  # Importa el módulo requests, aunque no se use directamente aquí
from configs.def_main import *
from func_bin import *
from pyrogram import filters # Importa los filtros

@ryas("bin")
async def bin_command(client: Client, message: types.Message):
    """
    Busca información sobre un BIN y devuelve una respuesta formateada.

    Args:
        client: El objeto Client de Pyrogram para interactuar con Telegram.
        message: El objeto Message de Pyrogram que contiene el mensaje del usuario.
    """
    try:
        # Extrae el número de BIN del mensaje.
        parts = message.text.split()
        if len(parts) < 2:
            await message.reply_text("Por favor, proporciona un número de BIN válido después del comando .bin")
            return
        bin_number = parts[1][:6]
    except IndexError:
        await message.reply_text("Por favor, proporciona un número de BIN después del comando .bin")
        return
    except ValueError:
        await message.reply_text("Número de BIN inválido. Debe contener solo dígitos.")
        return

    # Busca el BIN en el diccionario.
    bin_info = get_bin_info(bin_number)

    if bin_info:
        # Si se encuentra el BIN, formatea la respuesta.
        user_id = message.from_user.id
        connection, cursor = connect_db()
        if connection and cursor:
            cursor.execute("""
                SELECT rango, lang
                FROM users
                WHERE user_id = %s
            """, (user_id,))
            user_data = cursor.fetchone()
            connection.close()
        else:
            user_data = ("Free", "es")

        rango_usuario = user_data[0] if user_data else "Free"
        lang_usuario = user_data[1] if user_data else "es"

        # Formatea la respuesta.
        if lang_usuario == "es":
            respuesta = (
                f" {bin_info['flag']} - Data For {bin_number} Found - \n"
                "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                f"#Bin{bin_number}\n"
                f"• Bank: {bin_info['bank_name']}\n"
                f"- Info: {bin_info['vendor']} - {bin_info['type']} - {bin_info['level']}\n"
                f"- Country: {bin_info['country']} ({bin_info['flag']})\n"
                "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                f"Req By: {message.from_user.username or message.from_user.first_name or 'Unknown'}[{rango_usuario}]"
            )
        else:
            respuesta = (
                f" {bin_info['flag']} - Data For {bin_number} Found - \n"
                "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                f"#Bin{bin_number}\n"
                f"• Bank: {bin_info['bank_name']}\n"
                f"- Info: {bin_info['vendor']} - {bin_info['type']} - {bin_info['level']}\n"
                f"- Country: {bin_info['country']} ({bin_info['flag']})\n"
                "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                f"Req By: {message.from_user.username or message.from_user.first_name or 'Unknown'}[{rango_usuario}]"
            )
        await message.reply_text(respuesta)
    else:
        if lang_usuario == "es":
            await message.reply_text(f"No se encontró información para el BIN {bin_number}.")
        else:
            await message.reply_text(f"No information found for BIN {bin_number}.")
