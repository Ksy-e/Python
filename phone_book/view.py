import controller

def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы',]
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню:'))
    return user_input

def show_contacts(phone_book: list):
    if len(phone_book)>0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} {item[2]}')
    else:
        print('Телефонная книга пустая или не загружена')

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохранена успешно')

def new_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def del_contact():
    del_name = input('Введите имя и фамилию контакта, который хотите удалить: ')
    return del_name

def result_del():
    print('Контакт удален успешно. Не забудьте сохранить файл!')

def change_contact():
    change = input('Какой контакт изменить? Введите имя : ')
    return change

def result_change():
    print('Контакт изменен успешно. Не забудьте сохранить файл!')

def changeable_contact(answer):
    if answer == 'true':
        print('Попробуйте снова ')
    else:
        print('Заполните новые данные')