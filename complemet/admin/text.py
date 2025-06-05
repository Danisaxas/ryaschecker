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

    # Obtener el archivo de idioma basado en el usuario
    user_id = message.from_user.id
    lang_data, buttons_data = load_language_file(user_id)
    
    lang_files = ["es.json", "en.json", "fr.json", "de.json", "ru.json", "pt.json", "it.json", "ja.json", "ko.json", "mx.json", "pt.json", "tr.json", "vi.json", "ch.json"]

    for lang_file in lang_files:
        file_path = os.path.join("locales", lang_file)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Añadir el nuevo texto al archivo
            data[key] = text

            # Modificar el formato de cierre
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                
        except Exception as e:
            await message.reply_text(f"Error updating {lang_file}: {str(e)}")
            return

    await message.reply_text(f"Text '{text}' added successfully for key '{key}' in all languages.")
