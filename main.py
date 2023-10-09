from file_handler import FileHandler
from notes_manager import NotesManager
from cli_interface import CLIInterface

if __name__ == "__main__":
    file_handler = FileHandler("notes.json")
    manager = NotesManager(file_handler)
    interface = CLIInterface(manager)
    interface.run()
