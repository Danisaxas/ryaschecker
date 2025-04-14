from pyrogram import Client, types, filters
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from classBot.MongoDB import MondB
from _date import *

@Astro("bin")
async def bin_command(client: Client, message: types.Message):
    try:
        user_id = message.from_user.id
        user_data = MondB(idchat=user_id).queryUser()
        if user_data:
            lang = user_data.get('lang', 'es')
            ban_status = user_data.get('status', 'Libre')
            razon = user_data.get('razon', "")
        else:
            lang = 'es'
            ban_status = 'No'
            razon = ""
        if lang == 'es':
            text_dict = text_es
        elif lang == 'en':
            text_dict = text_en
        else:
            text_dict = text_es
        if ban_status == 'No':
            parts = message.text.split()
            if len(parts) < 2:
                await message.reply_text(text_dict['bin_usage'], reply_to_message_id=message.id)
                return
            bin_number = parts[1][:6]
        else:
            await message.reply_text(
                text_dict['block_message'].format(user_id=user_id, razon=razon),
                reply_to_message_id=message.id
            )
            return
    except IndexError:
        if lang == 'es':
            text_dict = text_es
        elif lang == 'en':
            text_dict = text_en
        else:
            text_dict = text_es
        await message.reply_text(text_dict['bin_usage'], reply_to_message_id=message.id)
        return
    except ValueError:
        if lang == 'es':
            text_dict = text_es
        elif lang == 'en':
            text_dict = text_en
        else:
            text_dict = text_es
        await message.reply_text(text_dict['bin_error'], reply_to_message_id=message.id)
        return
    bin_info = get_bin_info(bin_number)
    if bin_info:
        user_id = message.from_user.id
        user_data = MondB(idchat=user_id).queryUser()
        rango_usuario = user_data.get('role', 'Free User') if user_data else "Free User"
        respuesta = text_dict['bin_message'].format(
            bandera=bin_info['flag'],
            bin_number=bin_number,
            bank_name=bin_info['bank_name'],
            vendor=bin_info['vendor'],
            type=bin_info['type'],
            level=bin_info['level'],
            pais=bin_info['country'],
            pais_codigo=bin_info['iso'],
            username=message.from_user.username or message.from_user.first_name or 'Unknown',
            rango=rango_usuario
        )
        await message.reply_text(respuesta, reply_to_message_id=message.id)
    else:
        await message.reply_text(text_dict['bin_not_found'].format(bin_number=bin_number), reply_to_message_id=message.id)