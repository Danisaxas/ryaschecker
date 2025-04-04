from configs.def_main import * # Importa las variables y funciones necesarias

@ryasbt("^lenguaje$")
async def handle_lenguaje_button(client: Client, callback_query: types.CallbackQuery):
    """
    Muestra el menú de idiomas disponibles.
    """
    try:
        await callback_query.message.edit(
            text="Estos son los lenguajes disponibles:",
            reply_markup=lang
        )
    except Exception as e:
        await callback_query.message.edit(
            text=f"Ocurrió un error: {e}",
            reply_markup=None
        )
