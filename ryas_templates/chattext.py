# ryas_templates/chattext.py

# Español
es = {
    'idtext': '''<b>
Ryas Chk </> ID de Usuario [🌹]
- - - - - - - - - - - - - -
Nombre de Usuario: @{username}
ID: <code>{user_id}</code>
Chat_ID: <code>{chat_id}</code>
- - - - - - - - - - - - - - 
<code>Bot por: @Exzzex 🌸</code>
</b>''',

    'metext': '''<b>
Ryas Chk ⺢ => Info de Usuario
- - - - - - - - - - - - - - - - - - - - - 
⺢ Usuario:
Nombre de Usuario: @{username} [<code>{user_id}</code>]
Nombre: {firts_name} | Baneo: No
- - - - - - - - - - - - - - - - - - - - - 
⺢ Membresía:
Rol: {rango} | Créditos: {creditos}
Antispam: {antispam}
Expiración: 0
</b>''',

    'register_not': '''<b> No estás registrado en la base de datos, usa /register</b>''',

    'startx': '''<b>
¡Hola! {username} 🍄, Bienvenido a RyasChk. ¡Relájate y recarga energías!
- - - - - - - -
Hoy es: 
{caracas_time} 💤
- - - - - - - -
[🇪🇸] @{username}, ¿listo para usar Ryas? Soy tu bot personal para chequear tarjetas. Usa /cmds para ver qué puedo hacer.
- - - - - - - -
</b>''',

    'tools': '''<b>
Herramientas de RyasChk / Página 1
- - - - - - - -
Generador de Bines:
Formato: $gen 601120  
Condición: ¡Desconectado! ❌
- - - - - - - -
Sk Ckeck:
Formato: $sk sk_live 
Condición: ¡Desconectado! ❌
- - - - - - - -
Buscador de BINs:
Formato: $bin 601120 
Condición: ¡Desconectado! ❌
- - - - - - - -
Generador de Direcciones:
Formato: $dir Código_de_País 
Condición: ¡Desconectado! ❌
- - - - - - - -
Verificación de Fraude de IP:
Formato: $ip 1.1.1.1 
Condición: ¡Desconectado! ❌
- - - - - - - -
</b>''',

    'informacion_text': '''<b>
Información de RyasChk ! 🌩
- - - - - - - -
Última Actualización: 04/04/25
Idiomas Disponibles: Español, Inglés
Desarrollador: @Exzzex
Fecha de Creación del Bot: 10/10/2024
</b>''',
    'description_text': '''<b>
Descripción de Ryas ! 🌩
- - - - - - - - -
Canales:
Onyx Updates: @próximamente
Canal de Referencias de Onyx: @coming soon
Usuarios Gratis de Onyx: @próximamente
- - - - - - - - - - - -
Información de Ryas:
- - - - -
Desarrollador: @Exzzex ✅ | [Comprar]
Dev Note: ¡Hola chicos, esta es la nueva versión de onyx, hecha con velocidad y buena experiencia de chequeo en mente!
- - - - -
Vendedores:
@coming soon | coming soon ✅ | [Buy]
- - - - - - - - - - - -
Onyx Updates:
Versión: 1.3.0 [✅]
Update: próximamente p.m (GMT-5) [✅]
- - - - - - - - - - - -
Reportar problemas a: @Astrozdev
</b>''',

    'close_text': '''<b>
¡Adiós! 🌩
- - - - - - - - - - - -
Disfruta mi uso.
</b>''',

    'not_privilegios': '''<b> No cuentas con los privilegios suficientes para usar este comando</b>''',

    'msgformat': '''<b>[<a href='t.me/ryascheckerbot'>⺢</a>] AdminHub: $msg id or all !texto</b>''',

    'vryas': '''<b>¡Hola! {name} 🍄, Bienvenido al Sistema Vryas Acá podrás seleccionar tu lenguaje y ver más info del bot
- - - - - - - - - - - -
Actualmente RyasChk se encuentra en estado ONN✅ Dando lo mejor del bot se encuentra en la version 1.0.1
- - - - - - - - - - - -
Última Actualización:
04/04/25 > 05:30 (🇻🇪)</b>''',
    'registerx': '''<b>あ » Interactúa con el bot sin ningún inconveniente, si deseas más información, usa los siguientes comandos. 

↯ » Precios: /pricings
↯ » Más información: /data</b>''',
    'already_registered': '<b>あ » User {user} se encuentra registrado en la Base de Datos.</b>', # Mensaje de registro existente
    'setpriv_usage': "Uso correcto: /setpriv <ID> <Privilegio>",
    'setpriv_value_error': "El ID y el privilegio deben ser números.",
    'setpriv_success': "Privilegio actualizado correctamente para el ID {user_id}.",
    'setpriv_not_found': "Ese ID no se encuentra en la base de datos.",
    'gen_response': '''💳 Tus Tarjetas Generadas 💳
- - - - - - - - - - - - - - - - - - - - - - -
BIN: {bin_prefix}
- - - - - - - - - - - - - - - - - - - - - - -
Banco: {banco}
Marca: {marca}
Tipo: {tipo}
País: {pais} ({pais_codigo})
- - - - - - - - - - - - - - - - - - - - - - -

{tarjetas}

Req By: @{username} [{rango}]
''',
    'ban_message': '''Ryas Chk  Panel de Administrador [⚠️]
- - - - - - - - - - - - - - -
<b>Usuario Baneado</b>
Usuario: @{username} [{target_user_id}]
Razón: {ban_reason}
Administrador: @{admin_username} [{admin_id}]''',
    'ban_usage': "Uso correcto: /ban <ID> <razón>",
    'ban_validation': "El ID de usuario debe ser un número entero.",
    'unban_message': '''Ryas Chk  Panel de Administrador [⚠️]
- - - - - - - - - - - - - - -
<b>Usuario Desbaneado</b>
Usuario: @{username} [{target_user_id}]
Fecha:  {fecha}
Administrador: @{admin_username} [{admin_id}]''',
    'unban_usage': "Uso correcto: /unban <ID>",
    'unban_validation': "User ID must be an integer.",
    'block_message': "Usuario baneado ⚠️\nID: {user_id} \nRazón: {razon}",
    'lang_message': "Idiomas disponibles en Ryas Chk \nTu idioma actual es: {idioma_actual}"
}

# Inglés
en = {
    'idtext': '''<b>
Ryas Chk </> User ID [🌹]
- - - - - - - - - - - - - -
Username: @{username}
ID: <code>{user_id}</code>
Chat_ID: <code>{chat_id}</code>
- - - - - - - - - - - - - -
<code>Bot by: @Exzzex 🌸</code>
</b>''',

    'metext': '''<b>
Ryas Chk ⺢ => User Info
- - - - - - - - - - - - - - - - - - - - -
⺢ User:
Username: @{username} [<code>{user_id}</code>]
First Name: {firts_name} | Ban: No
- - - - - - - - - - - - - - - - - - - - -
⺢ Membership:
Role: {rango} | Credits: {creditos}
Antispam: {antispam}
Expiration: 0
</b>''',

    'register_not': '''<b> You are not registered in the database, use /register</b>''',

    'startx': '''<b>
Hello! {username} 🍄, Welcome to RyasChk. Relax and recharge your energy!
- - - - - - - -
Today is: 
{caracas_time} 💤
- - - - - - - -
[🇺🇸] @{username}, ready to use Ryas? I'm your personal bot for checking cards. Use /cmds to see what I can do.
- - - - - - - -
</b>''',

    'tools': '''<b>
RyasChk Tools / Page 1
- - - - - - - -
Bin Generator:
Format: $gen 601120  
Condition: Offline! ❌
- - - - - - - -
Sk Ckeck:
Format: $sk sk_live 
Condition: Offline! ❌
- - - - - - - -
BIN Lookup:
Format: $bin 601120 
Condition: Offline! ❌
- - - - - - - -
Gen Address:
Format: $dir Country_code 
Condition: Offline! ❌
- - - - - - - -
IP Fraud Check:
Format: $ip 1.1.1.1 
Condition: Offline! ❌
- - - - - - - -
</b>''',

    'informacion_text': '''<b>
Ryas Description ! 🌩
- - - - - - - -
Bot Information:
Last Update: 04/04/25
Available Languages: English, Spanish
Developer: @Exzzex
Bot Creation Date: 10/10/2024
</b>''',
    'description_text': '''<b>
Ryas Description ! 🌩
- - - - - - - - -
Channels:
Onyx Updates: @coming soon
Onyx References channel: @coming soon
Onyx Free Users: @coming soon
- - - - - - - - - - - -
Ryas Information:
- - - - -
Dev: @Exzzex ✅ | [Buy]
Dev Note: Hi guys, this is the new version of onyx, made with speed and good checking experience in mind!
- - - - -
Sellers:
@coming soon | coming soon ✅ | [Buy]
- - - - - - - - - - - -
Onyx Updates:
Version: 1.3.0 [✅]
Update: coming soon p.m (GMT-5) [✅]
- - - - - - - - - - - -
Report problems to: @Astrozdev
</b>''',

    'close_text': '''<b>
Good bye! 🌩
- - - - - - - - - - - -
Enjoy my use.
</b>''',

    'not_privilegios': '''<b> You do not have sufficient privileges to use this command</b>''',

    'msgformat': '''<b>[<a href='t.me/ryascheckerbot'>⺢</a>] AdminHub: $msg id or all !texto</b>''',

    'vryas': '''<b>Hello! {name} 🍄, Welcome to the Vryas System Here you can select your language and see more info of the bot
- - - - - - - - - - - -
Currently RyasChk is ONN✅ Giving the best of the bot is in version 1.0.1
- - - - - - - - - - - -
Last Update:
04/04/25 > 05:30 (🇻🇪)</b>''',
    'registerx': '''<b>あ » Interact with the bot without any problems, if you want more information, use the following commands.

↯ » Prices: /pricings
↯ » More information: /data</b>''',
    'already_registered': '<b>あ » User {user} is already registered in the Database.</b>', # Added existing registration message
    'setpriv_usage': "Correct usage: /setpriv <ID> <Privilege>",
    'setpriv_value_error': "ID and privilege must be numbers.",
    'setpriv_success': "Privilege updated correctly for ID {user_id}.",
    'setpriv_not_found': "That ID is not found in the database.",
    'gen_response': '''💳 Your Generated Cards 💳
- - - - - - - - - - - - - - - - - - - - - - -
BIN: {bin_prefix}
- - - - - - - - - - - - - - - - - - - - - - -
Bank: {banco}
Brand: {marca}
Type: {tipo}
Country: {pais} ({pais_codigo})
- - - - - - - - - - - - - - - - - - - - - - -

{tarjetas}

Req By: @{username} [{rango}]
''',
    'ban_message': '''Ryas Chk  Admin Panel [⚠️]
- - - - - - - - - - - - - - -
<b>User Banned</b>
User: @{username} [{target_user_id}]
Reason: {ban_reason}
Admin: @{admin_username} [{admin_id}]''',
    'ban_usage': "Correct usage: /ban <ID> <reason>",
    'ban_validation': "User ID must be an integer.",
    'unban_message': '''Ryas Chk  Admin Panel [⚠️]
- - - - - - - - - - - - - - -
<b>User Unbanned</b>
User: @{username} [{target_user_id}]
Date:  {fecha}
Admin: @{admin_username} [{admin_id}]''',
    'unban_usage': "Correct usage: /unban <ID>",
    'unban_validation': "User ID must be an integer.",
    'block_message': "User blocked ⚠️\nID: {user_id} \nReason: {razon}",
    'lang_message': "Available languages in Ryas Chk \nYour current language is: {idioma_actual}"
}
