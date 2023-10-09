import json
import os

class FileHandler:
    """Обработчик файлов"""

    def __init__(self, filename):
        self.filename = filename

    def load(self):
        """Загрузка данных из файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save(self, data):
        """Сохранение данных в файл"""
        with open(self.filename, 'w') as file:
            json.dump(data, file)
