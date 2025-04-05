import os
import logging
from pyrogram import Client
from configs.def_main import *
import asyncio
from datetime import datetime
import pytz  # Importa pytz
from pyrogram.errors import RPCError # Importa la clase base de las excepciones de Pyrogram

logging.basicConfig(level=logging.INFO)

Ryas = Client(
    "Ryas",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root=PLUGIN_ROOT)
)

OWNER_ID_INT = 8150119370 # definir directamente el id

@Ryas.on_callback_query()
async def callpri(client, callback_query):
    if (
        callback_query.message.reply_to_message 
        and callback_query.message.reply_to_message.from_user.id != callback_query.from_user.id
    ):
        await callback_query.answer("❗️ Access denied ❗️")
        return
    
    await callback_query.continue_propagation()

async def main():
    async with Ryas:
        # Obtener la fecha y hora de inicio en la zona horaria de Caracas
        caracas_timezone = pytz.timezone("America/Caracas")
        now = datetime.now(caracas_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")
        
        try:
            # Intenta enviar el mensaje directamente
            await Ryas.send_message(
                chat_id=OWNER_ID_INT,
                text=f"RyasChk ha encendido.\nEl estado del bot es ONN ✅\nHora de encendido: {now}"
            )
            logging.info("Bot started and notification sent to owner.")
        except RPCError as e:
            # Si da un error de RPC, obtener la información del usuario y reintentar
            if "PEER_ID_INVALID" in str(e) or "USER_ID_INVALID" in str(e) or "KEY_ERROR" in str(e): # incluir KEY_ERROR
                try:
                    owner_user = await Ryas.get_users(OWNER_ID_INT)
                    await Ryas.send_message(
                        chat_id=owner_user.id,  # Usa el ID de usuario de get_users
                        text=f"RyasChk ha encendido.\nEl estado del bot es ONN ✅\nHora de encendido: {now}"
                    )
                    logging.info("Bot started, user info fetched, and notification sent to owner.")
                except Exception as e2:
                    # Manejar cualquier otro error al obtener el usuario o enviar el mensaje
                    logging.error(f"Error sending startup message: {e2}")
            else:
                logging.error(f"Error sending startup message: {e}")

    
Ryas.run(main())
