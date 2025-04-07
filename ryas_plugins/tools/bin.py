from pyrogram import Client, types, filters
import requests
from configs.def_main import * # Asegúrate de que esto funcione con Pyrogram
from func_bin import *
import sqlite3

@ryas("bin")
async def bin_command(client: Client, message: types.Message):
    """
    Busca información sobre un BIN y devuelve una respuesta formateada.
    """
    connection = None
    cursor = None
    try:
        connection, cursor = connect_db()
        user_id = message.from_user.id
        cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'
        ban_status = result[1] if result else 'No' #obtener el estado de baneo
        razon = result[2] if result else ""
        reply_msg_id = message.reply_to_message.message_id if message.reply_to_message else message.id
        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict
        
        if ban_status == 'Yes': #verificar si el usuario esta baneado
            await message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=reply_msg_id
            )
            return
                
            
            return
        parts = message.text.split()
        if len(parts) < 2:
            if lang == 'es':
                from ryas_templates.chattext import es as text_dict
            elif lang == 'en':
                from ryas_templates.chattext import en as text_dict
            else:
                from ryas_templates.chattext import es as text_dict
            await message.reply_text(
                text_dict['bin_usage'],
                reply_to_message_id=reply_msg_id
            )
            return
        bin_number = parts[1][:6]
    except IndexError:
        lang = "es"
        if connection and cursor:
            cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            lang = result[0] if result else 'es'
            ban_status = result[1] if result else 'No' #obtener el estado de baneo
            razon = result[2] if result else ""
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict
        await message.reply_text(
            text_dict['bin_usage'],
            reply_to_message_id=reply_msg_id
        )
        return
    except ValueError:
        lang = "es"
        if connection and cursor:
            cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            lang = result[0] if result else 'es'
            ban_status = result[1] if result else 'No' #obtener el estado de baneo
            razon = result[2] if result else ""
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict
        await message.reply_text(
            text_dict['bin_error'],
            reply_to_message_id=reply_msg_id
        )
        return

    # Busca el BIN en el diccionario.
    bin_info = get_bin_info(bin_number)
    if connection and cursor:
        cursor.execute("SELECT lang, ban, razon FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        lang = result[0] if result else 'es'
        ban_status = result[1] if result else 'No' #obtener el estado de baneo
        razon = result[2] if result else ""
    if lang == 'es':
        from ryas_templates.chattext import es as text_dict
    elif lang == 'en':
        from ryas_templates.chattext import en as text_dict
    else:
        from ryas_templates.chattext import es as text_dict

    if bin_info:
        user_id = message.from_user.id
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
            username=message.from_user.username or message.from_user.first_name or 'Unknown',
            rango=rango_usuario
        )
        await message.reply_text(respuesta)
    else:
        await message.reply_text(
            text_dict['bin_not_found'].format(bin_number=bin_number),
            reply_to_message_id=reply_msg_id
        )
