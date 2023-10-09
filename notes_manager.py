from file_handler import FileHandler
from note import Note

class NotesManager:
    """Класс для управления заметками"""

    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.notes = [Note.from_dict(data) for data in self.file_handler.load()]

    def add(self, note):
        """Добавление заметки"""
        self.notes.append(note)
        self._save()

    def update(self, index, note):
        """Обновление заметки по индексу"""
        self.notes[index] = note
        self._save()

    def delete(self, index):
        """Удаление заметки по индексу"""
        del self.notes[index]
        self._save()

    def _save(self):
        """Сохранение всех заметок в файл"""
        self.file_handler.save([note.to_dict() for note in self.notes])
