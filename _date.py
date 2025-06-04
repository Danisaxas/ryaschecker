from pyrogram import Client,filters
from pyrogram import *
import time, logging,requests
from func_bin import *
from func_gen import *
import re, random,asyncio
from classBot.MongoDB import MondB
import time, pytz
from datetime import datetime
from func_gen import *
from func_bin import *
import json
import os

def Astro(bit:str= None):
    nix = Client.on_message(filters.command(bit, ["/", ".", ",","-","$","%","&"]))
    return nix

def AstroButton(bit:str= None):
    nix = Client.on_callback_query(filters.regex(bit)) # type: ignore
    return nix

_hasd = '3ed76d05d92a5203ca076066146a47bc'
_tokn= '7555371279:AAFH3aSAR9yqiLm5nbD36q3TorpdFzJQKPY'
owner= '7732700923'
_channel= '-1002364228833'
_plugin_root= 'complemet'
video = 'https://i.imgur.com/Ewq69ET.gif'

loogs = logging.basicConfig(level=logging.INFO)

print(requests.get('https://translate.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&es=en&q=hellow&tbb=1&ie=UTF-8&oe=UTF-8').text)

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

IDIOMA_CAPITAL_MAP = {
    "mx": ("Mexico City", "Mexico", "America/Mexico_City"),
    "es": ("Madrid", "Spain", "Europe/Madrid"),
    "en": ("Washington DC", "United States", "America/New_York"),
    "tr": ("Ankara", "Turkey", "Europe/Istanbul"),
    "ru": ("Moscow", "Russia", "Europe/Moscow"),
    "pt": ("Lisbon", "Portugal", "Europe/Lisbon"),
    "ko": ("Seoul", "South Korea", "Asia/Seoul"),
    "ch": ("Beijing", "China", "Asia/Shanghai"),
    "fr": ("Paris", "France", "Europe/Paris"),
    "de": ("Berlin", "Germany", "Europe/Berlin"),
    "vi": ("Hanoi", "Vietnam", "Asia/Bangkok"),
    "id": ("Jakarta", "Indonesia", "Asia/Jakarta"),
    "it": ("Rome", "Italy", "Europe/Rome"),
    "ja": ("Tokyo", "Japan", "Asia/Tokyo"),
    "ar": ("Riyadh", "Saudi Arabia", "Asia/Riyadh"),
}

def get_capital_time(lang_code: str) -> str:
    lang_code = lang_code.lower()
    if lang_code not in IDIOMA_CAPITAL_MAP:
        city, country, tz = "Caracas", "Venezuela", "America/Caracas"
    else:
        city, country, tz = IDIOMA_CAPITAL_MAP[lang_code]
    tz_obj = pytz.timezone(tz)
    now = datetime.now(tz_obj)
    return now.strftime(f"%Y-%m-%d {city}, {country} %I:%M %p")

def load_language_file(user_id, default_lang="es"):
    from classBot.MongoDB import MondB
    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else default_lang) or default_lang
    lang = lang.lower()
    
    # Base path de _date.py
    base_path = os.path.dirname(os.path.abspath(__file__))  
    
    # Cambiado para acceder correctamente a /app/locales
    locales_path = os.path.abspath(os.path.join(base_path, "..", "locales"))  # /app/locales
    
    # Ruta completa del archivo del idioma
    lang_file = os.path.join(locales_path, f"{lang}.json")
    
    try:
        # Intentamos abrir el archivo del idioma específico
        with open(lang_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        # Si no se encuentra, cargamos el español por defecto
        with open(os.path.join(locales_path, "es.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        return data