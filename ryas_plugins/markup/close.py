from configs.def_main import *
@ryasbt("^close$")
async def description(client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        close_text
    )
