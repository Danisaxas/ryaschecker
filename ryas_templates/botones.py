from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# English Language Buttons
en = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Tools", callback_data="tools"),
            InlineKeyboardButton("Information", callback_data="description")
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
    
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Languages", callback_data="lenguaje"),
        ]
        ]),
    
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Back", callback_data="home")
        ]
    ]),
    
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Do you want to generate again?", callback_data="re_gen"),
            InlineKeyboardButton("bot channel", url="t.me/Astrozdev")
        ]
    ]),
    
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("bot channel", callback_data="channel_link")
        ]
    ]),

    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Description", callback_data="informacion"),
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
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Auth", callback_data="Auth"),
                InlineKeyboardButton("Charge", callback_data="Charge"),
                InlineKeyboardButton("CCN Gates", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("Mass Checking", callback_data="Mass_Check"),
                InlineKeyboardButton("Back", callback_data="home")
            ]
        ]
    ),

}

# Spanish Language Buttons
es = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Herramientas", callback_data="tools"),
            InlineKeyboardButton("Informacion", callback_data="description")
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
    
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Idiomas", callback_data="lenguaje"),
        ]
        ]),
    
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Atras", callback_data="home")
        ]
    ]),

    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("¿Quieres generar de nuevo?", callback_data="re_gen"),
            InlineKeyboardButton("bot canal", url="t.me/Astrozdev")
        ]
    ]),
    
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("bot canal", callback_data="channel_link")
        ]
    ]),

    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Descripcion", callback_data="informacion"),
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
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Auth", callback_data="Auth"),
                InlineKeyboardButton("Charge", callback_data="Charge"),
                InlineKeyboardButton("CCN Gates", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("Mass Checking", callback_data="Mass_Check"),
                InlineKeyboardButton("Atrás", callback_data="home")
            ]
        ]
    ),
}
