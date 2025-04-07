from pyrogram import Client, types
import requests
from configs.def_main import *
from func_bin import *
from pyrogram import filters

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
            # Cargar el texto en el idioma correspondiente
            lang = "es"  # Reemplazar con la lógica para obtener el idioma del usuario
            if lang == 'es':
                from ryas_templates.chattext import es as text_dict
            elif lang == 'en':
                from ryas_templates.chattext import en as text_dict
            else:
                from ryas_templates.chattext import es as text_dict  # Por defecto español
            await message.reply_text(text_dict['bin_usage'])
            return
        bin_number = parts[1][:6]
    except IndexError:
        lang = "es"  # Reemplazar con la lógica para obtener el idioma del usuario
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict  # Por defecto español
        await message.reply_text(text_dict['bin_usage'])
        return
    except ValueError:
        lang = "es"  # Reemplazar con la lógica para obtener el idioma del usuario
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict  # Por defecto español
        await message.reply_text(text_dict['bin_error'])
        return

    # Busca el BIN en el diccionario.
    bin_info = get_bin_info(bin_number)
    lang = "es"  # Reemplazar con la lógica para obtener el idioma del usuario
    if lang == 'es':
        from ryas_templates.chattext import es as text_dict
    elif lang == 'en':
        from ryas_templates.chattext import en as text_dict
    else:
        from ryas_templates.chattext import es as text_dict  # Por defecto español

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

        respuesta = text_dict['bin_message'].format(
            bandera=bin_info['flag'],
            bin_number=bin_number,
            bank_name=bin_info['bank_name'],
            vendor=bin_info['vendor'],
            type=bin_info['type'],
            level=bin_info['level'],
            pais=bin_info['country'],
            pais_codigo=bin_info['iso'],  # Asegúrate de que 'iso' sea el código del país
            username=message.from_user.username or message.from_user.first_name or 'Unknown',
            rango=rango_usuario
        )
        await message.reply_text(respuesta)
    else:
        await message.reply_text(text_dict['bin_not_found'].format(bin_number=bin_number))
