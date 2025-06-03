from _date import *
from Source_pack.BoutnAll import pt as botones_pt
from classBot.MongoDB import MondB

@AstroButton("^pt$")
async def handle_pt_button(client: Client, callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        db = MondB(idchat=user_id)
        _database = db._client['bot']
        _collection = _database['user']
        _collection.update_one({"_id": user_id}, {"$set": {"lang": "pt"}})
        await callback_query.message.edit_text(
            """Cloud DB | LANG [🇧🇷]

Sucesso! Agora seu idioma selecionado é [Português]!""",
            reply_markup=botones_pt['back_lang']
        )
    except Exception as e:
        await callback_query.message.edit_text(f"Ocorreu um erro: {e}")
    finally:
        db._client.close()
