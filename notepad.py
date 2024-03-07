# Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку,
# сохранять её, читать список заметок, редактировать заметку, удалять заметку.

import json
import os
from datetime import datetime

# определение количества записей
def load_data():
    if os.path.exists("book.json"):
        with open("book.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []
    
# сохранение файла
def save_data(data):
    with open("book.json", "w") as file:
        json.dump(data, file, indent=4)

# ввод данных
def enter_head():
    return input("Введите заголовок заметки : ").title()

def enter_memo():
    return input("Введите тело заметки: ").title()

def enter_data():
    data = load_data()
    new_data = {}
    new_data["id"] = len(data)+1
    new_data["head"] = enter_head()
    new_data["memo"] = enter_memo()
    new_data["time"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    data.append(new_data)
    save_data(data)
    print("Заметка успешно создана!")

# вывод данных
def print_data():
    with open('book.json', 'r', encoding='utf-8') as file:
        print(file.read())

# редактор
def edit_data():
    print('Выберете поле для редактирования:\n'
        '1. Заголовок\n'
        '2. Заметка')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Необходимо отредактировать: ').title()
    empty = []
    print("Найдено:\n")
    with open('book.csv', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                
                print(item, end="\n\n")
        with open('book.csv', 'w', encoding='utf-8') as file:   #удаляет всё
            file.write('\n'.join(empty))
            new_data = item.replace(item, '')
            with open ('book.csv', 'w') as file:
                file.write(new_data)

# редактор
def edit_data(id):
    data = load_data()
    for arra in data:
        if arra["id"] == id:
            arra["head"] = input("Новый заголовок заметки: ")
            arra["memo"] = input("Новая заметка: ")
            arra["time"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            save_data(data)
            print("Заметка успешно отредактирована")
            return
    print("Этой заметки уже нет")

# удаление данных
def delete_data(id):
    data = load_data()
    data = [arra for arra in data if arra["id"] != id]
    save_data(data)
    print("Заметка успешно удалена!")

# интерфейс
def interface():
    cmd = 0
    while cmd != '5':
        print("Введите команду: \n"
            "1. Добавить заметку\n"
            "2. Вывести все заметки\n"
            "3. Редактирование заметки\n"
            "4. Удаление заметки\n"
            "5. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            cmd = input("Введите действие: ")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                edit_data(int(input("Введите id заметки для редактирования: ")))
            case '4':
                delete_data(int(input("Введите id заметки для удаления: ")))
            case '5':
                print('Всего доброго! ')

interface()