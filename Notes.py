import json
import os
import datetime


file_name = 'notes.json'


# Для создания нового файла, если его нет
def create_notes_file():
    with open(file_name, "w") as file:
        json.dump([], file)

# Функция для создания новой заметки
def create_note(notes, title, message):
    note_id = len(notes) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "message": message, "timestamp": timestamp}
    notes.append(note)
    return notes


# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(file_name, "w") as file:
        json.dump(notes, file, indent=4)


# Для чтения заметок из файла
def load_notes():
    try:
        with open(file_name, "r") as file:
            notes = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        create_notes_file()
        notes = []
    return notes


# Для редактирования заметки
def edit_note(notes, note_id, new_title, new_message):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["message"] = new_message
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    else:
        print("Заметки с таким ID нет.")
    return notes


# Для удаления заметки
def delete_note(notes, note_id):
    notes = [note for note in notes if note["id"] != note_id]
    return notes


# Функция для показа содержимого заметки по ID
def show_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            print(
                f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['message']}, Время создания: {note['timestamp']}")
            break
    else:
        print("Заметки с таким ID нет.")

def main():
    notes = load_notes()
    info = ('Вам доступны следующие команды: \n'
            'info - показывает актуальные команды\n'
            'add - добавление заметки в файл\n'
            'read - чтение заметки\n'
            'edit - можно внести изменения в заметку\n'
            'delete - удаляет заметку с выбранным ID\n'
            'show - показывает заметки по ID\n'
            'exit - выход из программы')

    while True:
        command = input("Введите команду (info, add, read, edit, delete, show, exit): ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            notes = create_note(notes, title, message)
            save_notes(notes)
            print("Заметка успешно сохранена.")
        elif command == "read":
            for note in notes:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")
        elif command == "edit":
            note_id = int(input("Введите ID заметки которую хотите изменить: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новый текст заметки: ")
            notes = edit_note(notes, note_id, new_title, new_message)
            save_notes(notes)
            print("Заметка успешно изменина.")
        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = delete_note(notes, note_id)
            save_notes(notes)
            print("Заметка успешно удалена.")
        elif command == "show":
            note_id = int(input("Введите ID заметки для просмотра: "))
            show_note(notes, note_id)
        elif command == "info":
            print(info)
        elif command == "exit":
            break
        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()