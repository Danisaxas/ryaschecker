from _date import *
from classBot.MongoDB import MondB
from Source_pack.TextAll import en as text_en
from Source_pack.TextAll import es as text_es
from Source_pack.TextAll import pt as text_pt
from Source_pack.TextAll import ru as text_ru
from Source_pack.TextAll import zh as text_zh
from Source_pack.TextAll import ko as text_ko
from Source_pack.TextAll import fr as text_fr
from Source_pack.TextAll import de as text_de
from Source_pack.TextAll import tr as text_tr
from Source_pack.TextAll import ja as text_ja
from Source_pack.TextAll import ar as text_ar
from Source_pack.TextAll import it as text_it
from Source_pack.TextAll import es_mx as text_es_mx
from pyrogram.types import Message

IDIOMAS_VALIDOS = ["es", "en", "pt", "ru", "zh", "ko", "fr", "de", "tr", "ja", "ar", "it", "es_mx"]

@Astro("setlang")
async def comando_setlang(client, message: Message):
    user_id = message.from_user.id
    user_data = MondB(idchat=user_id).queryUser()

    lang = user_data.get("lang", "es") if user_data else "es"
    lang = lang.lower()
    for code in IDIOMAS_VALIDOS:
        if lang.startswith(code):
            lang = code
            break
    else:
        lang = "es"

    text = {
        "es": text_es,
        "en": text_en,
        "pt": text_pt,
        "ru": text_ru,
        "zh": text_zh,
        "ko": text_ko,
        "fr": text_fr,
        "de": text_de,
        "tr": text_tr,
        "ja": text_ja,
        "ar": text_ar,
        "it": text_it,
        "es_mx": text_es_mx,
    }[lang]

    if str(user_id) != str(owner):
        await message.reply_text(
            text['setrol_no_permission'],
            reply_to_message_id=message.id
        )
        return

    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text(text['setlang_usage'], reply_to_message_id=message.id)
        return

    try:
        target_id = int(args[1])
    except ValueError:
        await message.reply_text(text['setlang_invalid_id'], reply_to_message_id=message.id)
        return

    nuevo_idioma = args[2].lower()
    if nuevo_idioma not in IDIOMAS_VALIDOS:
        await message.reply_text(text['setlang_invalid_lang'], reply_to_message_id=message.id)
        return

    db = MondB(idchat=target_id)
    _database = db._client['bot']
    _collection = _database['user']

    target_user = _collection.find_one({"_id": target_id})
    if not target_user:
        await message.reply_text(text['setlang_not_found'], reply_to_message_id=message.id)
        db._client.close()
        return

    _collection.update_one({"_id": target_id}, {"$set": {"lang": nuevo_idioma}})

    await message.reply_text(
        text['setlang_success'].format(id=target_id, idioma=nuevo_idioma),
        reply_to_message_id=message.id
    )
    db._client.close()