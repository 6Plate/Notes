
import datetime

class Note():
    
    def __init__ (self, name, content):
        self.id = -1
        self.name = name
        self.content = content
        self.date = datetime.date.today()
    
    
    def name(self):
        return self.name

    @title.setter
    def name(self, name):
        self.name = name

    @property
    def content(self):
        return self.content

    @text.setter
    def content(self, content):
        self.content = content

    @property
    def getId(self):
        return self.id

    @note_id.setter
    def setId(self, id):
        self.id = id

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, date):
        self.date = date

    def __str__(self):
        return f'\nЗаметка: {self._note_id}\nДата создания(редактирования):'\
            f' {self._date}\nЗаголовок: {self._title}\nТело: {self._text}\n'