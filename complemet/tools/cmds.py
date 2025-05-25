from _date import *
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en

@Astro("cmds")
async def cmds_command(client, message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser ()
    
    if user_data:
        lang = user_data.get('lang', 'es')
    else:
        lang = 'es'  # Default to Spanish if user data is not found

    text_dict = text_es if lang == 'es' else text_en

    await message.reply_text(text_dict['command_list'], reply_to_message_id=message.id)
