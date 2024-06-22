import random

from ..BotClasses import Command as command_class
from ..BotClasses import User, Message
from ..BotClasses.Keyboards import keyboard
# from ..BotClasses.Stage_handler import Stage
from clients.tg.api import TgClient

async def processor(user: User, message: Message, tg_client: TgClient, callback_query=False, stage=None):
    msg = """Вы можете узнать ответы на часто задаваемые вопросы по ссылке ниже"""
    await tg_client.send_message(message.chat['id'], msg, buttons=keyboard('faq', user).get_link())
    return


command = command_class()

command.keys = ['вопросы и ответы', 'вопрос', 'помоги', 'помощь', 'help' 'часто задаваемые вопросы']
command.process = processor
command.payload = []
