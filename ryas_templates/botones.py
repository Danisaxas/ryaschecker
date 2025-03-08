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
