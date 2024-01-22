import json
import datetime as dt
from .User import User

main_keyboard = [
    ["Реактивный бот"],
    ["Купить/поддержка"],
]

subscribe = [[['Открыть', 'https://t.me/+WncZ5PybI9I5YzAy']]]
support_button = [[['Чат с поддержкой', 'https://t.me/reactive_tg_bot']]]
reactive_bot_landing = [[['Презентация', 'https://bookingandrent.ru/reactive_bot']]]



class keyboard:
    def __init__(self, type_name: str, user: User, buttons: list = None, payload=None):
        self.type_name = type_name
        self.buttons = []
        self.user = user
        if self.type_name == 'main_keyboard':
            self.buttons = main_keyboard

        elif self.type_name == 'exit':
            self.buttons = exit
        elif self.type_name == 'subscribe_button':
            self.buttons = subscribe
        elif self.type_name == 'support_button':
            self.buttons = support_button
        elif self.type_name == 'reactive_bot_landing':
            self.buttons = reactive_bot_landing



    def get_inline_keyboard(self) -> dict:
        button_list = []
        for button_row in self.buttons:
            button_row_list = []
            for button in button_row:
                callback_data = "{" + f'"button":"{button[1]}","data":"{button[-1]}"' + "}"
                button_ = {
                    'text': button[0],
                    'callback_data': callback_data
                }
                button_row_list.append(button_)
            button_list.append(button_row_list)
        keyboard = {"inline_keyboard": button_list}
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard

    def get_keyboard(self) -> list:
        if not len(self.buttons):
            keyboard = {
                'remove_keyboard': True
            }
            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))
            return keyboard
        buttons_massive = []
        for layer in self.buttons:
            layer_massive = []
            for button in layer:
                layer_massive.append(self.get_button(button))
            buttons_massive.append(layer_massive)
        keyboard = {
            'resize_keyboard': True,
            'one_time': True,
            'keyboard': self.buttons

        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard

    def get_link(self) -> list:
        button_list = []
        for button_row in self.buttons:
            button_row_list = []
            for button in button_row:
                button_ = {
                    'text': button[0],
                    'url': button[1]
                }
                button_row_list.append(button_)
            button_list.append(button_row_list)
        keyboard = {"inline_keyboard": button_list}
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard

    def get_button(self, text):
        return {'text': text}
