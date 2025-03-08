from configs.def_main import *
@ryasbt("^tools$")
async def tools_callback(client, callback_query: CallbackQuery):
    # Envía el menú de herramientas
    await callback_query.message.edit_text(
        tools,
        reply_markup=atras
    )

@ryasbt("^home$")
async def home_callback(client, callback_query: CallbackQuery):
    # Obtiene el nombre de usuario y la hora de Caracas
    username = callback_query.from_user.username or "Usuario"
    caracas_time = datetime.now(pytz.timezone("America/Caracas")).strftime("%Y-%m-%d Venezuela, Caracas %I:%M %p")

    # Regresa al mensaje de inicio
    await callback_query.message.edit_text(
        startx.format(username=username, caracas_time=caracas_time),
        reply_markup=mainstart
    )
