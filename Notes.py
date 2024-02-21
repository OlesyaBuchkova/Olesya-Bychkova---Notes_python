import json
from csv import DictReader
from datetime import datetime

from numpy.distutils.misc_util import get_info
file_name = 'notes.json'


def create_file(): #Создание файла, если его нет
    with open(file_name, "w", encoding='utf-8') as file:
        json.dump([], file)

def save_notes(notes): #сохранение заметки
    with open(file_name, "w") as file:
        json.dump(notes, file, indent=4)


def create_note(notes, title, message): #Создание новой заметки
    note_id = len(notes) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "message": message, "timestamp": timestamp}
    notes.append(note)
    return notes





def main():
    notes = load_notes()
    info = ('Вам доступны следующие команды: \n'
            'info - показывает актуальные команды\n'
            'add - добавление заметки в файл\n'
            'read - чтение заметки\n'
            'delete - удаляет заметку с выбранным ID\n'
            'edit - можно внести изменения в заметку\n'
            'date - показывает заметки созданные, в указанных датах\n'
            'all - показывает все заметки\n'
            'exit - выход из программы')

    while True:
        command = input("Введите команду: info, add, read, delete, edit, data, all, exit): ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            notes = create_file(notes, title, message)
            save_notes(notes)
            print("Заметка успешно сохранена.")
        elif command == "read":
            for note in notes:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")
        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новый текст заметки: ")
            notes = edit_note(notes, note_id, new_title, new_message)
            save_notes(notes)
            print("Заметка успешно отредактирована.")
        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = delete_note(notes, note_id)
            save_notes(notes)
            print("Заметка успешно удалена.")
        elif command == "all":
            note_id = int(input("Введите ID заметки для просмотра: "))
            show_note(notes, note_id)
        elif command == "date":
            show_date(notes)
        elif command == "info":
            print(info)
        elif command == "exit":
            break

        else:
            print("Невозможно выполнить команду, для просомтра всех доступных коман введите info")



