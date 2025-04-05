import os
import logging
from pyrogram import Client
from configs.def_main import *
import asyncio
from datetime import datetime

Ryas = Client(
    "Ryas",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root=PLUGIN_ROOT)
)

@Ryas.on_callback_query()
async def callpri(client, callback_query):
    if (
        callback_query.message.reply_to_message 
        and callback_query.message.reply_to_message.from_user.id != callback_query.from_user.id
    ):
        await callback_query.answer("❗️ Access denied ❗️")
        return
    
    await callback_query.continue_propagation()

logging.basicConfig(level=logging.INFO)

Ryas.run()
