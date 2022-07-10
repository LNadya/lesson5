"""
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
"""
import os
import shutil
import sys

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        for i in range(3):
            # проверка на существование
            if not os.path.exists(f'new{i}'):
                # сздать папку передаем путь
                os.mkdir(f'new{i}')
        # создать новый файл
        new_file1 = open("new_file1.py", "w")
        new_file1.close()
        new_file2 = open("new_file2.txt", "w")
        new_file2.close()
        # список файлов и папок
        print(os.listdir())

    elif choice == '2':
        for i in range(2):
            # удалить папку
            os.rmdir(f'new{i}')
        # удалить новый файл
        os.remove("new_file2.txt")
        # список файлов и папок
        print(os.listdir())

    elif choice == '3':
        # копирование файла
        shutil.copyfile('new_file1.py', 'new_file1_copy.py')
        # копирование папки
        shutil.copytree('new2', 'new2_copy')
        # список файлов и папок
        print(os.listdir())

    elif choice == '4':
        print(os.listdir())

    elif choice == '5':
        dirname = 'G:/Университет искусственного интеллекта/Python разработчик/lesson5'
        dirfiles = os.listdir(dirname)
        fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

        dirs = []
        for file in fullpaths:
            if os.path.isdir(file): dirs.append(file)
        print(list(dirs))

    elif choice == '6':
        for oot, dirs, files in os.walk('G:/Университет искусственного интеллекта/Python разработчик/lesson5'):
            for filename in files:
                print(filename)

    elif choice == '7':
        print(sys.platform)

    elif choice == '8':
        print(os.getlogin())

    elif choice == '9':
        import victory

    elif choice == '10':
        import use_functions

    elif choice == '11':
        os.mkdir('G:/Университет искусственного интеллекта/Python разработчик/lesson5_new_directory')
        os.chdir('G:/Университет искусственного интеллекта/Python разработчик/lesson5_new_directory')

    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')