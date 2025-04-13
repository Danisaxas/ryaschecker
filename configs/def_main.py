
def ryas(bit):
    nix = Client.on_message(filters.command(bit, ["/", "+", "(", ")", "!", "?", "¿", "`", "~", "*", "#", "$", "_", "^", "°", "=", ".", ",", "-", "%", "@", "&", ":", ";", "<", ">", "[", "]", "{", "}", "|", "€", "£", "¢","¥", "™", "½", "¼", "§", "±", "!", "¿", "«", "»", "•", "†", "‡", "⁂", "∗", "√", "∞", "≈", "≠", "≡", "∩", "∪", "⊕", "⊗", "→", "←", "↑", "↓","⇐", "⇒", "⇔", "⇕", "✦", "✧", "✩", "✪"]))
    return nix

def ryasbt(bor):
    nox = Client.on_callback_query(filters.regex(bor))
    return nox

    
API_ID = "27533879"
API_HASH = "80029e88381fe5c63e364687906458a0"
BOT_TOKEN = "7555371279:AAHU_Pb6NNFEokKC4TlHci784NulynQ86zs"
PLUGIN_ROOT = "ryas_plugins"
LOGS_CHANNEL ="-1002364228833"
OWNER_ID ="8150119370"

