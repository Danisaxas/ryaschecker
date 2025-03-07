from configs.def_main import *
@ryas('id')
def obtener_id(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username if message.from_user.username else "No username"
    reply_msg = message.reply_to_message.message_id if message.reply_to_message else message.id

    message.reply_text(idtext.format(user_id=user_id, chat_id=chat_id, username=username), reply_to_message_id=reply_msg)