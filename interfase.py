from exp import *
from write import *
from delete import *
from rewrite import *
import datetime

def Button_Click():
    
    while (True):
        print('Введите команду:\
            \n1 - Добавить заметку\
            \n2 - Вывести список заметок\
            \n3 - Удалить заметку\
            \n4 - Редактировать заметку\
            \n5 - Выход')
        command = input()
        if command == '1':
            if (file_list()):
                for i in file_list():
                    j = int(i['ID'])
                j += 1
            else:
                j = 1
            head = input('Введите заголовок заметки: ')
            body = input('Введите тело заметки: ')
            now = datetime.datetime.now()
            add_data(f'{str(j)};{head};{body};{str(now)}')
        elif command == '2':
            print(write(file_list()))
        elif command == '3':
            print(write(file_list()))
            dell_id = int(input('Введите идентификатор заметки: '))
            dell_id -= 1
            dell_data(file_list(), dell_id)
        elif command == '4':
            print(write(file_list()))
            rew_id = int(input('Введите идентификатор заметки: '))
            rew_id -= 1
            head = input('Введите заголовок заметки: ')
            body = input('Введите тело заметки: ')
            rewrite(file_list(), rew_id, head, body)
        elif command == '5':
            break
            