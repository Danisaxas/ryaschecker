from configs.def_main import *
from pyrogram import Client, types
import mysql.connector
from datetime import datetime

@ryas('register')
async def register_user(client: Client, message: types.Message):
    """
    Registra a un usuario en la base de datos y muestra un mensaje de bienvenida en su idioma.
    """
    user_id = message.from_user.id
    username = message.from_user.username or "Desconocido"
    lang = message.from_user.language_code or "es"
    lang = lang if isinstance(lang, str) else "es"

    connection = None
    try:
        connection, cursor = connect_db()
        
        # Insertar usuario en la base de datos
        cursor.execute("""
            INSERT INTO users (
                user_id, rango, privilegio, creditos, antispam, expiracion, dias,
                bin_lasted, ban, fecha_registro, lang
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)
        """, (user_id, 'Free User', 0, 0, True, None, 0, None, 'No', lang))
        connection.commit()
        
        # Cargar el texto en el idioma correspondiente
        if lang == 'es':
            from ryas_templates.chattext import es as text_dict
        elif lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict #por defecto español

        registro_msg = text_dict['registerx'].format(username=username, user_id=user_id, lang=lang.upper())
        log_msg = f"""
✅ ¡Nuevo Registro!
━━━━━━━━━━━━━
👤 Usuario: @{username}
🆔 ID: {user_id}
⺢ Fecha: {datetime.now().strftime('%Y-%m-%d')}
🌍 Idioma: {lang}
━━━━━━━━━━━━━
🎯 ¡Bienvenido a RyasChk!
"""

        await message.reply_text(registro_msg)
        await client.send_message(LOGS_CHANNEL, log_msg)

    except mysql.connector.IntegrityError:
        # Obtener el idioma del usuario del mensaje
        user_lang = message.from_user.language_code or 'es' #por defecto español
        if user_lang.startswith('en'):
            user_lang = 'en'
        else:
            user_lang = 'es'
        if user_lang == 'en':
            from ryas_templates.chattext import en as text_dict
        else:
            from ryas_templates.chattext import es as text_dict
        await message.reply_text(en['already_registered'].format(user=username) if user_lang == 'en' else es['already_registered'].format(user=username))
    except Exception as e:
        print(f"Error en register_user: {e}")
        await message.reply_text(f"Ocurrió un error durante el registro: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
