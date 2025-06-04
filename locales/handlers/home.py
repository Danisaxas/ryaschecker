from _date import *
from classBot.MongoDB import MondB
import json
import os

@AstroButton("^home$")
async def handle_home(client, callback_query):
    user = callback_query.from_user
    user_id = user.id

    user_data = MondB(idchat=user_id).queryUser()
    lang = (user_data.get("lang") if user_data else "es") or "es"
    lang = lang.lower()

    data, buttons_data = load_language_file(user_id)

    startx_template = data.get("startx", "")
    message = startx_template.format(
        caracas_time=caracas_time(lang),
        idioma_actual=LANGUAGES_FLAGS.get(lang, '🏳️‍🌈'),
        username=user.username or user.first_name
    )

    await callback_query.message.edit_text(message)
    await callback_query.answer()
