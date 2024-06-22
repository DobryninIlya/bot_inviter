import random

from ..BotClasses import Command as command_class
from ..BotClasses import User, Message
from ..BotClasses.Keyboards import keyboard
# from ..BotClasses.Stage_handler import Stage
from clients.tg.api import TgClient

async def processor(user: User, message: Message, tg_client: TgClient, callback_query=False, stage=None):
    msg = """Вы также можете посетить наш сайт, нажав на кнопку ниже"""
    await tg_client.send_message(message.chat['id'], msg, buttons=keyboard('site', user).get_link())
    return


command = command_class()

command.keys = ['сайт', 'наш сайт', 'открыть сайт']
command.process = processor
command.payload = []
