import random

from ..BotClasses import Command as command_class
from ..BotClasses import User, Message
from ..BotClasses.Keyboards import keyboard
# from ..BotClasses.Stage_handler import Stage
from clients.tg.api import TgClient


async def processor(user: User, message: Message, tg_client: TgClient, callback_query=False, stage=None):
    msg = """
🧑🏻‍💻Бот-менеджер онлайн-сервиса *GetMeCar* поможет Вам подобрать и забронировать транспорт (авто, байки, яхты, вертолёты и др.) в 35 странах, популярных для отдыха и работы. Предложения представлены локальными прокатными компаниями и частными владельцами.

В нашем каталоге более 10 000 предложений аренды транспорта и техники.

В меню есть три варианта помочь вам подобрать и забронировать транспорт."""
    await tg_client.send_message(user.id, msg, buttons=keyboard('main', user).get_keyboard(), parse_mode=True)
    return



command = command_class()

command.keys = ['start', '/start', 'начать', 'выход']
command.process = processor
command.payload = []
