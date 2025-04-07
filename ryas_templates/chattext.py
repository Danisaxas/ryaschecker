# ryas_templates/chattext.py

# Español
es = {
    'idtext': '''<b>
Ryas Chk </> ID de Usuario [🌹]
- - - - - - - - - - - - - - - - - - - - - - - - - - 
Nombre de Usuario: @{username}
ID: <code>{user_id}</code>
Chat_ID: <code>{chat_id}</code>
- - - - - - - - - - - - - - - - - - - - - - - - - - 
<code>Bot por: @Exzzex 🌸</code>
</b>''',

    'metext': '''<b>
Ryas Chk ⺢ => Info de Usuario
- - - - - - - - - - - - - - - - - - - - - - - - - - 
⺢ Usuario:
Nombre de Usuario: @{username} [<code>{user_id}</code>]
Nombre: {firts_name} | Baneo: No
- - - - - - - - - - - - - - - - - - - - - - - - - - 
⺢ Membresía:
Rol: {rango} | Créditos: {creditos}
Antispam: {antispam}
Expiración: 0
</b>''',

    'register_not': '''<b> No estás registrado en la base de datos, usa /register</b>''',

    'startx': '''<b>
Bienvenido Ryas dev Bot  |  <code>{caracas_time}</code>
                                                                             
[{idioma_actual}] Hola @{username} Bienvenido a Ryas Telegram Bot, las puertas de enlace, las herramientas y las funciones se agregan constantemente, para saber que mis diferentes comandos usan los botones que se muestran aquí:
━━━━━━━━━━━━━
<code>Api Bot El estado es: Online ✅ | Ryas Api ¡Está en línea!!</code>
</b>''',

    'tools': '''<b>
Herramientas de RyasChk / Página 1
━━━━━━━━━━━━
Generador de Bines:
Formato: $gen 601120  
Condición: ¡Desconectado! ❌
━━━━━━━━━━━━
Sk Ckeck:
Formato: $sk sk_live 
Condición: ¡Desconectado! ❌
━━━━━━━━━━━━
Buscador de BINs:
Formato: $bin 601120 
Condición: ¡Desconectado! ❌
━━━━━━━━━━━━
Generador de Direcciones:
Formato: $dir Código_de_País 
Condición: ¡Desconectado! ❌
━━━━━━━━━━━━
Verificación de Fraude de IP:
Formato: $ip 1.1.1.1 
Condición: ¡Desconectado! ❌
━━━━━━━━━━━━
</b>''',

    'informacion_text': '''<b>
Información de RyasChk ! 🌩
━━━━━━━━━━━━
Última Actualización: 04/04/25
Idiomas Disponibles: Español, Inglés
Desarrollador: @Exzzex
Fecha de Creación del Bot: 10/10/2024
</b>''',
    'description_text': '''<b>
Descripción de Ryas ! 🌩
━━━━━━━━━━━━
Canales:
Onyx Updates: @próximamente
Canal de Referencias de Onyx: @próximamente
Usuarios Gratis de Onyx: @próximamente
━━━━━━━━━━━━━━━━━
Información de Ryas:
━━━━━━━
Desarrollador: @Exzzex ✅ | [Comprar]
Dev Note: ¡Hola chicos, esta es la nueva versión de onyx, hecha con velocidad y buena experiencia de chequeo en mente!
━━━━━━━
Vendedores:
@coming soon | coming soon ✅ | [Buy]
━━━━━━━━━━━━━━━━━
Onyx Updates:
Versión: 1.3.0 [✅]
Update: próximamente p.m (GMT-5) [✅]
━━━━━━━━━━━━━━━━━
Reporta problemas a: @Exzzex
</b>''',

    'close_text': '''<b>
¡Adiós! 🌩
━━━━━━━━━━━━━━━━━
Disfruta mi uso.
</b>''',

    'not_privilegios': '''<b> No cuentas con los privilegios suficientes para usar este comando</b>''',

    'msgformat': '''<b>[<a href='t.me/ryascheckerbot'>⺢</a>] AdminHub: $msg id or all !texto</b>''',

    'ryas_cloud': '''<b>
>_ $Comenzar_ Ryas Cloud | Bienvenido @{username} - Cloud DB 

[🇪🇸] Bienvenido a la nueva suscripción de Ryas Cloud, sus datos compartidos en la nube con Ryas se almacenarán aquí, navegue a través de los botones para descubrir qué es lo nuevo que tenemos para usted:      

<code>Ryas Cloud Version:  0.0.1</code>  | Ryas Cloud Plan:  <code>Premium Cloud</code></b>''',
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
    'lang_message': '''
Bienvenido @{username} - Cloud DB | LANG [{idioma_actual}] 

Estos son los datos sobre su idioma guardado en el DB, ¿desea cambiar?Seleccione un nuevo idioma en los botones a continuación:''',
    'bin_not_found': "No se encontró información para el BIN {bin_number}.",
    'bin_usage': "Por favor, proporciona un número de BIN válido después del comando .bin",
    'bin_error': "Número de BIN inválido. Debe contener solo dígitos.",
    'bin_message': "<b>({bandera}) - Datos para <code>{bin_number}</code> encontró -</b> \n"
                   "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                   "<b>#Bin<code>{bin_number}</b></code>\n"
                   "<b>• Banco: <code>{bank_name}</b></code>\n"
                   "<b>• Informacion: <code>{vendor} - {type} - {level}</b></code>\n"
                   "<b>• Pais: <code>{pais} ({bandera})</b></code>\n"
                   "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                   "<b>Req By: @{username} [{rango}]</b>",
}

# Inglés
en = {
    'idtext': '''<b>
Ryas Chk </> User ID [🌹]
- - - - - - - - - - - - - - - - - - - - - - - - - - 
Username: @{username}
ID: <code>{user_id}</code>
Chat_ID: <code>{chat_id}</code>
- - - - - - - - - - - - - - - - - - - - - - - - - - 
<code>Bot by: @Exzzex 🌸</code>
</b>''',

    'metext': '''<b>
Ryas Chk ⺢ => User Info
- - - - - - - - - - - - - - - - - - - - - - - - - - 
⺢ User:
Username: @{username} [<code>{user_id}</code>]
First Name: {firts_name} | Ban: No
- - - - - - - - - - - - - - - - - - - - - - - - - - 
⺢ Membership:
Role: {rango} | Credits: {creditos}
Antispam: {antispam}
Expiration: 0
</b>''',

    'register_not': '''<b> You are not registered in the database, use /register</b>''',

    'startx': '''<b>
Welcome to Ryas dev Bot  |  <code>{caracas_time}</code>
                                                                             
[{idioma_actual}] Hello @Username welcome to Ryas telegram bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here:
━━━━━━━━━━━━━
<code>Api Bot Status is: Online ✅ | Ryas Api is Online!!</code>
</b>''',

    'tools': '''<b>
RyasChk Tools / Page 1
━━━━━━━━━━━━
Bin Generator:
Format: $gen 601120  
Condition: Offline! ❌
━━━━━━━━━━━━
Sk Ckeck:
Format: $sk sk_live 
Condition: Offline! ❌
━━━━━━━━━━━━
BIN Lookup:
Format: $bin 601120  
Condition: Offline! ❌
━━━━━━━━━━━━
Gen Address:
Format: $dir Country_code 
Condition: Offline! ❌
━━━━━━━━━━━━
IP Fraud Check:
Format: $ip 1.1.1.1 
Condition: Offline! ❌
━━━━━━━━━━━━
</b>''',

    'informacion_text': '''<b>
Ryas Description ! 🌩
━━━━━━━━━━━━
Bot Information:
Last Update: 04/04/25
Available Languages: English, Spanish
Developer: @Exzzex
Bot Creation Date: 10/10/2024
</b>''',
    'description_text': '''<b>
Ryas Description ! 🌩
━━━━━━━━━━━━
Channels:
Onyx Updates: @coming soon
Onyx References channel: @coming soon
Onyx Free Users: @coming soon
━━━━━━━━━━━━━━━━━
Ryas Information:
━━━━━━━
Dev: @Exzzex ✅ | [Buy]
Dev Note: Hi guys, this is the new version of onyx, made with speed and good checking experience in mind!
━━━━━━━
Sellers:
@coming soon | coming soon ✅ | [Buy]
━━━━━━━━━━━━━━━━━
Onyx Updates:
Version: 1.3.0 [✅]
Update: coming soon p.m (GMT-5) [✅]
━━━━━━━━━━━━━━━━━
Report problems to: @Exzzex
</b>''',

    'close_text': '''<b>
Good bye! 🌩
━━━━━━━━━━━━━━━━━
Enjoy my use.
</b>''',

    'not_privilegios': '''<b> You do not have sufficient privileges to use this command</b>''',

    'msgformat': '''<b>[<a href='t.me/ryascheckerbot'>⺢</a>] AdminHub: $msg id or all !texto</b>''',

    'ryas_cloud': '''<b>
>_ $Start_ Ryas Cloud | Welcome @{username} - Cloud DB

[🇺🇸] Welcome to the new Ryas Cloud subscription, your details shared in the cloud with Ryas will be stored here, navigate through the buttons to discover what's new we have for you:      

<code>Ryas Cloud Version:  0.0.1</code>  | Ryas Cloud Plan:  <code>Premium Cloud</code>
</b>''',
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
    'lang_message': '''
Welcome @{username} - Cloud DB | LANG [{idioma_actual}] 

These are the data about your language saved in the DB, do you want to change? Select a new language from the buttons below:''',
    'bin_not_found': "No information found for BIN {bin_number}.",
    'bin_usage': "Please provide a valid BIN number after the .bin command",
    'bin_error': "Invalid BIN number. It must contain only digits.",
    'bin_message': "<b>({bandera}) - Data For <code>{bin_number}</code> Found -</b> \n"
                   "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                   "<b>#Bin<code>{bin_number}</code></b>\n"
                   "<b>• Bank: <code>{bank_name}</code></b>\n"
                   "<b>• Info: <code>{vendor} - {type} - {level}</code></b>\n"
                   "<b>• Country: <code>{pais} ({bandera})</code></b>\n"
                   "- - - - - - - - - - - - - - - - - - - - - - - - - \n"
                   "<b>Req By: @{username} [{rango}]</b>",
}