from pyrogram.client import Client
from pyrogram import filters
from pyrogram import *
import time, logging, requests
from func_bin import *
from func_gen import *
import re, random, asyncio
from classBot.MongoDB import MondB
import time, pytz
from datetime import datetime
from func_gen import *
from func_bin import *
import os
import json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pycountry


def Astro(bit: str = None):
    nix = Client.on_message(filters.command(bit, ["/", ".", ",", "-", "$", "%", "&"]))
    return nix

def AstroButton(bit: str = None):
    nix = Client.on_callback_query(filters.regex(bit))
    return nix

_hasd = '3ed76d05d92a5203ca076066146a47bc'
_tokn = '7555371279:AAFH3aSAR9yqiLm5nbD36q3TorpdFzJQKPY'
owner = '7732700923'
_channel = '-1002364228833'
_plugin_root = 'complemet'
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

LANGUAGES_FLAGS = {
    "es": "🇪🇦",
    "en": "🇺🇲",
    "mx": "🇲🇽",
    "fr": "🇫🇷",
    "de": "🇩🇪",
    "pt": "🇵🇹",
    "it": "🇮🇹",
    "ja": "🇯🇵",
    "ko": "🇰🇷",
    "id": "🇮🇩",
    "ch": "🇨🇳",
    "vi": "🇻🇳",
    "ru": "🇷🇺",
    "tr": "🇹🇷",
    "ar": "🇸🇦",
}

import json
from classBot.MongoDB import MondB

import json
from classBot.MongoDB import MondB

import json
from classBot.MongoDB import MondB

def load_language_file(user_id):
    user = MondB(idchat=user_id).queryUser()
    lang = (user.get("lang") if user else "es") or "es"
    lang = lang.lower()

    if lang == "es":
        with open("locales/es.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/es.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "en":
        with open("locales/en.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/en.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "fr":
        with open("locales/fr.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/fr.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "de":
        with open("locales/de.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/de.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "ru":
        with open("locales/ru.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/ru.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "id":
        with open("locales/id.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/id.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "it":
        with open("locales/it.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/it.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "ja":
        with open("locales/ja.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/ja.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "ko":
        with open("locales/ko.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/ko.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "mx":
        with open("locales/mx.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/mx.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "pt":
        with open("locales/pt.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/pt.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "tr":
        with open("locales/tr.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/tr.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "vi":
        with open("locales/vi.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/vi.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "zh":
        with open("locales/zh.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/zh.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    elif lang == "ar":
        with open("locales/ar.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/ar.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)
    else:
        with open("locales/es.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("locales/button_layouts/es.json", "r", encoding="utf-8") as f:
            buttons_data = json.load(f)

    return data, buttons_data

def caracas_time(lang: str) -> str:
    timezones = {
        "es": ("Europe/Madrid", "Madrid, España"),
        "mx": ("America/Mexico_City", "Ciudad de México, México"),
        "en": ("America/New_York", "Washington D. C., United States"),
        "fr": ("Europe/Paris", "Paris, France"),
        "de": ("Europe/Berlin", "Berlin, Germany"),
        "pt": ("Europe/Lisbon", "Lisbon, Portugal"),
        "ru": ("Europe/Moscow", "Moscow, Russia"),
        "it": ("Europe/Rome", "Rome, Italy"),
        "ja": ("Asia/Tokyo", "Tokyo, Japan"),
        "ko": ("Asia/Seoul", "Seoul, South Korea"),
        "id": ("Asia/Jakarta", "Jakarta, Indonesia"),
        "zh": ("Asia/Shanghai", "Shanghai, China"),
        "vi": ("Asia/Ho_Chi_Minh", "Ho Chi Minh City, Vietnam"),
        "tr": ("Europe/Istanbul", "Istanbul, Turkey"),
        "ar": ("Asia/Dubai", "Dubai, UAE")
    }

    timezone, city = timezones.get(lang, ("America/Caracas", "Caracas, Venezuela"))

    timezone = pytz.timezone(timezone)
    time_in_city = datetime.now(timezone).strftime("%Y-%m-%d %I:%M:%S %p")
    return f"{time_in_city} {city}"

