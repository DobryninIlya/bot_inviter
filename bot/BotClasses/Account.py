import pyrogram
from pyrogram import errors

trigger_words = ['авто', 'арендую', 'аренда', 'аренды', 'аренду', 'арендовать', 'арендовал', 'арендовали', 'арендовала',
                 'арендовало', 'арендовано', 'арендована', 'арендован', 'арендованы', 'арендова'
                                                                                      'сниму']


class Telegram:
    def __init__(self, session_name: str, api_id: str, api_hash: str, proxy: dict):
        self.session_name = session_name
        self.app = pyrogram.Client(session_name, proxy=proxy, api_id=api_id, api_hash=api_hash)
        self.banned = False

    async def check_auth(self):
        try:
            await self.app.get_me()
        except pyrogram.errors.FloodWait as e:
            print('FloodWait:', e.x)
            self.banned = True
            return

    def send_reaction_to_message(self, chat_id, message_id, reaction):
        try:
            self.app.send_reaction(chat_id, message_id, reaction)
        except errors.FloodWait as e:
            print('FloodWait:', e.x)
            self.banned = True
            return
        except errors.RPCError as e:
            print('RPCError:', e)
            self.banned = True
            return
        except Exception as e:
            print('Exception:', e)
            self.banned = True
            return
        return

    async def join_chat(self, chat_id):
        try:
            await self.app.join_chat(chat_id)
        except errors.FloodWait as e:
            print('FloodWait:', e.x)
            print('___chat: '+chat_id)
            self.banned = True
            return
        except errors.RPCError as e:
            print('RPCError:', e)
            print('___chat: ' + chat_id)
            self.banned = True
            return
        except Exception as e:
            print('Exception:', e)
            print('___chat: ' + chat_id)
            self.banned = True
            return
        return
