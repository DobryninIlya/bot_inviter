import random

from ..BotClasses import Command as command_class
from ..BotClasses import User, Message
from ..BotClasses.Keyboards import keyboard
# from ..BotClasses.Stage_handler import Stage
from clients.tg.api import TgClient


async def processor(user: User, message: Message, tg_client: TgClient, callback_query=False, stage=None):
    msg = "Для ознакомления с возможностями реактивного бота воспользуйтесь нашей презентацией по кнопке ниже"
    await tg_client.send_message(user.id, msg, buttons=keyboard('reactive_bot_landing', user).get_link())
    return


command = command_class()

command.keys = ['реактивный бот', 'подробнее', 'инфо', 'информация']
command.process = processor
command.payload = []
