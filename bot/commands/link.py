import random

from ..BotClasses import Command as command_class
from ..BotClasses import User, Message
from ..BotClasses.Keyboards import keyboard
# from ..BotClasses.Stage_handler import Stage
from clients.tg.api import TgClient

file_path = 'group_id.txt'
async def processor(user: User, message: Message, tg_client: TgClient, callback_query=False, stage=None):
    with open(file_path, 'w') as file:
        file.write(str(message.chat['id']))
    msg = """Чат привязан"""
    await tg_client.send_message(message.chat['id'], msg, buttons=keyboard('null', user).get_keyboard())
    return


command = command_class()

command.keys = ['linkchat']
command.process = processor
command.payload = []
