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

def ryas(bit):
    nix = Client.on_message(filters.command(bit, ["/", "+", "(", ")", "!", "?", "¿", "`", "~", "*", "#", "$", "_", "^", "°", "=", ".", ",", "-", "%", "@", "&", ":", ";", "<", ">", "[", "]", "{", "}", "|", "€", "£", "¢","¥", "™", "½", "¼", "§", "±", "!", "¿", "«", "»", "•", "†", "‡", "⁂", "∗", "√", "∞", "≈", "≠", "≡", "∩", "∪", "⊕", "⊗", "→", "←", "↑", "↓","⇐", "⇒", "⇔", "⇕", "✦", "✧", "✩", "✪"]))
    return nix

def ryasbt(bor):
    nox = Client.on_callback_query(filters.regex(bor))
    return nox

    
API_ID = "27533879"
API_HASH = "80029e88381fe5c63e364687906458a0"
BOT_TOKEN = "7801858915:AAHyn1g1p7S9oMi8TPXV3yKGIDMNriXdXAQ"
PLUGIN_ROOT = "ryas_plugins"
LOGS_CHANNEL ="-1002388160660"