from configs.def_main import *
@ryasbt("^description$")
async def description(client, message):
    await message.reply_text(
        description_text,
        reply_to_message_id=message.id,
        reply_markup=back
    )
