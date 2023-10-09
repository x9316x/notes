from notes_manager import NotesManager
from note import Note

class CLIInterface:
    """Класс для консольного интерфейса"""

    def __init__(self, manager):
        self.manager = manager

    def run(self):
        """Основной цикл интерфейса"""
        while True:
            print("Команды:")
            print("1. Список заметок")
            print("2. Добавить заметку")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Выход")
            choice = input("Введите ваш выбор: ")

            if choice == "1":
                self.list_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                self.edit_note()
            elif choice == "4":
                self.delete_note()
            elif choice == "5":
                return
            else:
                print("Неверный выбор!")

    def list_notes(self):
        """Вывод списка заметок"""
        for index, note in enumerate(self.manager.notes):
            print(f"ID: {index}")
            print(f"Заголовок: {note.title}")
            print(f"Содержание: {note.content}")
            print(f"Дата: {note.date}")
            print("-" * 50)

    def add_note(self):
        """Добавление новой заметки"""
        title = input("Введите заголовок: ")
        content = input("Введите содержание: ")
        self.manager.add(Note(title, content))

    def edit_note(self):
        """Редактирование заметки"""
        index = int(input("Введите ID заметки для редактирования: "))
        title = input("Введите новый заголовок: ")
        content = input("Введите новое содержание: ")
        self.manager.update(index, Note(title, content))

    def delete_note(self):
        """Удаление заметки"""
        index = int(input("Введите ID заметки для удаления: "))
        self.manager.delete(index)
