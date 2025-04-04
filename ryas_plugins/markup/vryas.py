from configs.def_main import *

@ryasbt("^vryas$")
async def handle_vryas_button(client: Client, callback_query: types.CallbackQuery):
    name = callback_query.from_user.first_name or "Usuario"
    await callback_query.message.edit(
        text=vryas.format(name=name),
        reply_markup=vryasx # Añadir el teclado vryasx
    )
