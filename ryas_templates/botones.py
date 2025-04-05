from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainstart = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Gateways", callback_data="gateways"),
        InlineKeyboardButton("Tools", callback_data="tools"),
        InlineKeyboardButton("Description", callback_data="description")
    ],
    [
        InlineKeyboardButton("vRyas", callback_data="vryas"),
        InlineKeyboardButton("Close", callback_data="close")
    ]
])

atras = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Home", callback_data="home"),
        InlineKeyboardButton("Next", callback_data="next")
    ]
])

back = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("back", callback_data="home")
        ]
])

vryasx = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Informacion", callback_data="informacion"),
            InlineKeyboardButton("Lenguaje", callback_data="lenguaje"),
            InlineKeyboardButton("Home", callback_data="home")
        ]
    ]
)

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Inglés 🇺🇸", callback_data="en"),
            InlineKeyboardButton("Español 🇪🇸", callback_data="es")
        ]
    ]
)