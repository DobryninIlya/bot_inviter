from .Message import Message

class User:
    def __init__(self, update: Message):
        self.id = update.from_id
        self.name = update.first_name
        self.lastname = update.last_name
        try:
            self.username = update.username
        except:
            pass
        self.admLevel = 1


