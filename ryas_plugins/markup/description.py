from configs.def_main import *
@ryasbt("^description$")
async def description(client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        description_text,
        reply_markup=back
    )
