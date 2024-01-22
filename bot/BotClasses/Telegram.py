import asyncio
import time

from pyrogram import Client, idle
from . import Account
class TGAssembly:
    def __init__(self, accounts: list, chats: list, proxy: list):
        self.accounts = accounts
        self.chats = chats
        self.proxy = proxy

    async def join_chats(self):
        for chat in self.chats:
            for account in self.accounts:
                await account.join_chat(chat)
                await asyncio.sleep(3)

    def message_handler(self, client, message):
        print(f"Received message in chat {message.chat.id}: {message.text}")



    async def start(self):
        for account in self.accounts:
            await self.join_chats()

            @account.app.on_message()
            def on_message_handler(client, message):
                try:
                    account.send_reaction_to_message(message.chat.id, message.id, '🔥')
                    self.message_handler(client, message)
                except Exception as e:
                    print('Exception:', e)
                    # account.banned = True
                    return
            # await account.app.run()
            # await account.app.stop()
            # account.client.run()
