from pyrogram import Client, filters
from pyrogram import *
import time
import pytz
from datetime import datetime
from db.database import connect_db
import mysql.connector
from pyrogram.types import CallbackQuery
from ryas_templates.chattext import *
from ryas_templates.botones import *
from func_bin import *
from func_gen import *
import re
import random
import asyncio
from ryas_templates.chattext import en as text_dict
from ryas_templates.botones import en as botones_dict
from ryas_templates.chattext import es as text_dict
from ryas_templates.botones import es as botones_dict

def ryas(bit):
    nix = Client.on_message(filters.command(bit, ["/", "+", "(", ")", "!", "?", "¿", "`", "~", "*", "#", "$", "_", "^", "°", "=", ".", ",", "-", "%", "@", "&", ":", ";", "<", ">", "[", "]", "{", "}", "|", "€", "£", "¢","¥", "™", "½", "¼", "§", "±", "!", "¿", "«", "»", "•", "†", "‡", "⁂", "∗", "√", "∞", "≈", "≠", "≡", "∩", "∪", "⊕", "⊗", "→", "←", "↑", "↓","⇐", "⇒", "⇔", "⇕", "✦", "✧", "✩", "✪"]))
    return nix

def ryasbt(bor):
    nox = Client.on_callback_query(filters.regex(bor))
    return nox

    
API_ID = "27533879"
API_HASH = "80029e88381fe5c63e364687906458a0"
BOT_TOKEN = "7555371279:AAHU_Pb6NNFEokKC4TlHci784NulynQ86zs"
PLUGIN_ROOT = "ryas_plugins"
LOGS_CHANNEL ="-1002364228833"
OWNER_ID ="8150119370"

