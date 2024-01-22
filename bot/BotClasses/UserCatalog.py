from . import User, Account
import os
import traceback

FOLDER_PATH = 'user_options/'
ACCOUNTS = 'accounts/'
api_hash = "8da85b0d5bfe62527e5b244c209159c3"
api_id = "2496"


class UserCatalog:
    def __init__(self, user: User):
        self.user = user
        self.id = user.id
        self.folder_path = FOLDER_PATH + str(self.id)

    def make_folder(self):
        if not os.path.exists(self.folder_path):
            try:
                os.makedirs(self.folder_path)
                os.makedirs(self.folder_path + "/" + ACCOUNTS)
                print(f"Пользовательский каталог '{self.folder_path}' создан.")
            except OSError as e:
                print(f"Ошибка при создании папки по пути '{self.folder_path}': {e}")

    def get_chats(self):
        try:
            with open(self.folder_path + '/chats.txt', 'r') as file:
                chats = file.read()
                chats = chats.split('\n')
        except:
            chats = ''
        return chats

    def write_chats(self, chats: str):
        self.make_folder()
        with open(self.folder_path + '/chats.txt', 'w') as file:
            file.write(chats)

    def get_proxy(self):
        try:
            with open(self.folder_path + '/proxy.txt', 'r') as file:
                chats = file.read()
        except:
            chats = ''
        return chats

    def parse_proxy_list(self) -> list:
        proxy = self.get_proxy()
        proxy_list = proxy.split('\n')
        result = []
        for pr in proxy_list:
            try:
                params = pr.split(':')
                result.append({'ip': params[0], 'port': params[1], 'login': params[2], 'password': params[3]})
            except:
                print('Ошибка при парсинге прокси')
                traceback.print_exc()
        return result

    def write_proxy(self, chats: str):
        self.make_folder()
        with open(self.folder_path + '/proxy.txt', 'w') as file:
            file.write(chats)

    async def load_sessions_from_folder(self):
        sessions = []
        folder_path = FOLDER_PATH + str(self.id) + "/" + ACCOUNTS

        session_files = [f for f in os.listdir(folder_path) if f.endswith(".session")]

        for session_file in session_files:
            try:
                session_name = os.path.join(folder_path, os.path.splitext(session_file)[0])
                # Дополнительные параметры прокси, если необходимо
                proxy_settings = None

                account_info = Account.Telegram(session_name, api_id=api_id, api_hash=api_hash, proxy=proxy_settings)
                await account_info.app.start()
                await account_info.check_auth()
                sessions.append(account_info)
            except:
                print("Ошибка сессии: ")
                traceback.print_exc()


        return sessions
