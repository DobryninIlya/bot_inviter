import random

from ..BotClasses import Command as command_class
from ..BotClasses import User, Message
from ..BotClasses.Keyboards import keyboard
# from ..BotClasses.Stage_handler import Stage
from clients.tg.api import TgClient


async def processor(user: User, message: Message, tg_client: TgClient, callback_query=False, stage=None):
    msg = "Стоимость скачивания софта - 60$ (вечная лицензия). Для дополнительный вопросов и покупки софта, пожалуйста, свяжитесь с нами через @reactive_tg_bot"
    await tg_client.send_message(user.id, msg, buttons=keyboard('support_button', user).get_link())
    return


command = command_class()

command.keys = ['купить/поддержка', 'купить', 'как купить', 'цена']
command.process = processor
command.payload = []
