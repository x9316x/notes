import datetime

class Note:
    """Класс для представления заметки"""

    def __init__(self, title="", content=""):
        self.title = title
        self.content = content
        self.date = str(datetime.datetime.now())

    def to_dict(self):
        """Преобразование заметки в словарь"""
        return {
            "title": self.title,
            "content": self.content,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        """Создание заметки из словаря"""
        note = cls(data["title"], data["content"])
        note.date = data["date"]
        return note
