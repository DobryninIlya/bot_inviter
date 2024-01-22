from .User import User
from .Message import Message
from . import cursor, connection


class Stage:
    def __init__(self, user: User, message: Message):
        self.user_id = 0
        self.message = message
        self.cursor = cursor
        self.connectionection = connection
        self.cursor = cursor
        self.connection = connection
        self.user = user
        self.user_group_id = None
        self.user_group_name = None
        self.status = self._get_status_code()

    def _execute(self, sql_query):
        self.cursor.execute(sql_query)
        self.connection.commit()
        return

    def _get_status_code(self):
        sql = "SELECT Status FROM Status WHERE ID = {}".format(self.user_id)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if not result:
            return False
        result = result[0]
        return result

    def _set_status(self, code):
        if not code:
            self.cursor.execute("DELETE FROM Status WHERE ID={}".format(self.user_id))
            self.connection.commit()
            return
        try:
            self.cursor.execute("INSERT INTO Status VALUES ({},{})".format(self.user_id, code))
        except:
            self.cursor.execute("UPDATE Status SET Status = {} WHERE ID={}".format(code, self.user_id))
        finally:
            self.connection.commit()
