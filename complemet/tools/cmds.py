from _date import *
from classBot.MongoDB import MondB
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import en as text_en
from Source_pack.BoutnAll import en as btn_en
from Source_pack.BoutnAll import es as btn_es

@Astro("cmds")
async def cmds_command(client, message):
    user_id = message.from_user.id
    caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")
    user_data = MondB(idchat=user_id).queryUser ()
    
    if user_data:
        lang = user_data.get('lang', 'es')
        botones_dict = btn_es
    else:
        lang = 'es'
        botones_dict = btn_es

    text_dict = text_es if lang == 'es' else text_en

    await message.reply_text(text_dict['command_list'], reply_to_message_id=message.id, reply_markup=botones_dict['mainstart'])
