from _date import *
from classBot.MongoDB import MondB
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@AstroButton("^en$")
async def set_lang_en(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇺🇸 EN")

    db = MondB(idchat=user_id)
    db.update_user_lang("en")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^es$")
async def set_lang_es(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇪🇸 ES")

    db = MondB(idchat=user_id)
    db.update_user_lang("es")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^pt$")
async def set_lang_pt(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇧🇷 PT")

    db = MondB(idchat=user_id)
    db.update_user_lang("pt")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^ru$")
async def set_lang_ru(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇷🇺 RU")

    db = MondB(idchat=user_id)
    db.update_user_lang("ru")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^zh$")
async def set_lang_zh(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇨🇳 CH")

    db = MondB(idchat=user_id)
    db.update_user_lang("zh")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^ko$")
async def set_lang_ko(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇰🇷 KO")

    db = MondB(idchat=user_id)
    db.update_user_lang("ko")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^mx$")
async def set_lang_mx(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇲🇽 MX")

    db = MondB(idchat=user_id)
    db.update_user_lang("mx")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^fr$")
async def set_lang_fr(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇫🇷 FR")

    db = MondB(idchat=user_id)
    db.update_user_lang("fr")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^de$")
async def set_lang_de(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇩🇪 DE")

    db = MondB(idchat=user_id)
    db.update_user_lang("de")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^it$")
async def set_lang_it(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇮🇹 IT")

    db = MondB(idchat=user_id)
    db.update_user_lang("it")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^ja$")
async def set_lang_ja(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇯🇵 JA")

    db = MondB(idchat=user_id)
    db.update_user_lang("ja")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^tr$")
async def set_lang_tr(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇹🇷 TR")

    db = MondB(idchat=user_id)
    db.update_user_lang("tr")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^vi$")
async def set_lang_vi(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇻🇳 VI")

    db = MondB(idchat=user_id)
    db.update_user_lang("vi")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()

@AstroButton("^id$")
async def set_lang_id(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    lang_data = load_language_file(user_id)[0]  # Cargar el archivo de idioma
    data = lang_data.get("lang_success", "").format(username=user.username or user.first_name, idioma_actual="🇮🇩 ID")

    db = MondB(idchat=user_id)
    db.update_user_lang("id")

    back_lang_buttons = [
        [InlineKeyboardButton("Back", callback_data="back_lang")]
    ]

    await callback_query.message.edit_text(data, reply_markup=InlineKeyboardMarkup(back_lang_buttons))
    await callback_query.answer()
