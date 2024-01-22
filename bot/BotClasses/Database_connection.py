import traceback

# import psycopg2
import os
import sqlite3


class database_connections:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("/home/u_botkai/botraspisanie/botkai_telegram/bot/BotClasses/bot.db")
        except:
            self.connection = sqlite3.connect("bot/BotClasses/bot.db")

        self.cursor = self.connection.cursor()
        self.cursor.execute("""DELETE FROM Status""")
        self.connection.commit()


connect = database_connections()
cursor = connect.cursor
connection = connect.connection
