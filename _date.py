from pyrogram import Client,filters
from pyrogram import *
from Source_pack.text import *
from Source_pack.TextAll import *
from Source_pack.BoutnAll import *
import time, logging,requests
from func_bin import *
from func_gen import *
import re, random,asyncio
from classBot.MongoDB import MondB
import time, pytz
from datetime import datetime
from func_gen import *
from func_bin import *

def Astro(bit:str= None):
    nix = Client.on_message(filters.command(bit, ["/", ".", ",","-","$","%","&"]))
    return nix

def AstroButton(bit:str= None):
    nix = Client.on_callback_query(filters.regex(bit))
    return nix

_hasd = '3ed76d05d92a5203ca076066146a47bc'
_tokn= '7555371279:AAFH3aSAR9yqiLm5nbD36q3TorpdFzJQKPY'
_owner= '8150119370'
_channel= '-1002364228833'
_plugin_root= 'complemet'
video = 'https://i.imgur.com/Ewq69ET.gif'

loogs = logging.basicConfig(level=logging.INFO)

print(requests.get('https://translate.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&es=en&q=hellow&tbb=1&ie=UTF-8&oe=UTF-8').text)


def bin_chk(bina:int=None,chkby:str= None):
    req = requests.get(f'https://bins.antipublic.cc/bins/{bina}')
    if  "detail" in req.text:
        return f"<b>{req.json()['detail']}</b>"
    else:
        text = bintext.format(
                        req.json()['bin'],
                        req.json()['brand'],
                        req.json()['country_name'],
                        req.json()['country'],
                        req.json()['country_flag'],
                        req.json()['level'],
                        req.json()['type'],
                        req.json()['bank'],
                        chkby
                        )
        return text

def skey(
        data,
        headers,
        key:str=None,
        name:str=None
        ):

        pos = requests.post(f"https://api.stripe.com/v1/tokens",data=data, headers=headers, auth=(key, ""))
        if 'Invalid API Key provided' in pos.text:
            resp = sk.format('Dead ❌','Invalid API Key provided',name)
            return resp
        elif 'api_key_expired' in pos.text:
            resp = sk.format('Dead ❌','api_key_expired',name)
            return resp
        elif 'testmode_charges_only' in pos.text:
            resp = sk.format('Dead ❌','testmode_charges_only',name)
            return resp
        elif 'test_mode_live_card' in pos.text:
            resp = sk.format('Live ✅','test_mode_live_card',name)
            return resp
        else:
            resp = sk.format('Live ✅','Aprovado',name)
            return resp



usertime = {}
timetake = 15
def atspam(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if 5416957433 in usertime and time.time() - usertime[user_id] < timetake:
            await func(client, message)
            usertime[user_id] = time.time()
            return
        elif user_id in usertime and time.time() - usertime[user_id] < timetake:
            wait_time = int(timetake - (time.time() - usertime[user_id]))
            await message.reply(f"<b>₪ AntiFlood ⇝ <code>{wait_time} sg.</code> </b>")
            return
        else:
            await func(client, message)
            usertime[user_id] = time.time()

    return wrapper

def traducir_a_ingles(texto):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": "en",
        "dt": "t",
        "q": texto,
        "ie": "UTF-8",
        "oe": "UTF-8"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            return response.json()[0][0][0]
        except Exception:
            return "Error al procesar la respuesta."
    return f"Error en la solicitud: {response.status_code}"


