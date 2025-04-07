from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# English Language Buttons
en = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Tools", callback_data="tools"),
            InlineKeyboardButton("Description", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Close", callback_data="close")
        ]
    ]),

    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Home", callback_data="home"),
            InlineKeyboardButton("Next", callback_data="next")
        ]
    ]),

    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("back", callback_data="home")
        ]
    ]),
    
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Return", callback_data="homevR")
        ]
    ]),

    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Information", callback_data="informacion"),
                InlineKeyboardButton("Languages", callback_data="lenguaje"),
                InlineKeyboardButton("Back", callback_data="home")
            ]
        ]
    ),

    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("English [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("Español [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    )
}

# Spanish Language Buttons
es = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Herramientas", callback_data="tools"),
            InlineKeyboardButton("Descripción", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Cerrar", callback_data="close")
        ]
    ]),

    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Inicio", callback_data="home"),
            InlineKeyboardButton("Siguiente", callback_data="next")
        ]
    ]),

    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Atrás", callback_data="home")
        ]
    ]),
    
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Volver", callback_data="homevR")
        ]
    ]),

    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Información", callback_data="informacion"),
                InlineKeyboardButton("Idioma", callback_data="lenguaje"),
                InlineKeyboardButton("Atras", callback_data="home")
            ]
        ]
    ),

    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("English [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("Español [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    )
}
