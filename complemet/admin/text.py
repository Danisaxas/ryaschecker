from _date import *
from pyrogram.types import Message
import json
import os

@Astro("text")
async def set_text(client, message: Message):
    args = message.text.split(maxsplit=2)
    
    if len(args) < 3:
        await message.reply_text("Usage: /text \"<key>\" <text>")
        return
    
    key = args[1].strip('"')
    text = args[2]

    # Obtener el archivo de idioma
    user_id = message.from_user.id
    lang_data, buttons_data = load_language_file(user_id)

    # Archivos de idioma
    lang_files = [
        "locales/es.json", "locales/en.json", "locales/fr.json", "locales/de.json", 
        "locales/ru.json", "locales/pt.json", "locales/it.json", "locales/ja.json", 
        "locales/ko.json", "locales/mx.json", "locales/pt.json", "locales/tr.json", 
        "locales/vi.json", "locales/zh.json"
    ]

    for lang_file in lang_files:
        try:
            with open(lang_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Añadir el nuevo texto al archivo
            data[key] = text

            # Modificar el formato de cierre
            with open(lang_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                
        except Exception as e:
            await message.reply_text(f"Error updating {lang_file}: {str(e)}")
            return

    await message.reply_text(f"Text '{text}' added successfully for key '{key}' in all languages.")
