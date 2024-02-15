import random
from ..BotClasses import Command as command_class
from ..BotClasses import User, Message
from ..BotClasses.Keyboards import keyboard
# from ..BotClasses.Stage_handler import Stage
from clients.tg.api import TgClient


# domain = "https://t.me/chatinviter_robot/subscribe?startapp="
file = open("appdomain.secret", "r")
domain = file.read()

async def processor(user: User, message: Message, tg_client: TgClient, callback_query=False, stage=None):
    bot_landing = [[['Подписка', '']]]
    msg = """Привет! Я — бот-координатор проекта «Литература для сердца и разума», помогу тебе оформить подписку и попасть в закрытый канал и чат для подготовки к экзамену по литературе 🤍

Для начала нажми на «подписку» ниже ⬇️
"""
    bot_landing[0][0][1] = domain + "client_id%3Dtg" + str(user.id)
    await tg_client.send_message(user.id, msg, buttons=keyboard('bot_landing', user, buttons=bot_landing).get_link())
    return


command = command_class()

command.keys = ['/start', 'start', 'купить', 'подробнее', 'инфо', 'информация']
command.process = processor
command.payload = []
