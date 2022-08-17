import crud as cr
import logger as lg
import sys

print('\n Students ')

def ls_menu():
    while True:
        print('\nМЕНЮ:')
        print()
        print('1. Все записи')
        print('2. Поиск по фамилии')
        print('3. Поиск по группе')
        print('4. Поиск по курсу')
        print('5. Добавить запись')
        print('6. Редактировать')
        print('7. Удалить')
        print('8. Закрыть программу\n')
        n = сhecking_the_number(input('Пункт: '))

        if n == 1:
            lg.logging.info('Item number 1')
            print(cr.retrive())
            input()

        elif n == 2:
            lg.logging.info('Item number 2')
            search = input('Фамилия: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(surname=search))
            input()

        elif n == 3:
            lg.logging.info('Item number 3')
            search = input('Группа: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(group=search))
            input()

        elif n == 4:
            lg.logging.info('Item number 4')
            search = input('Курс: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(course=search))
            input()

        elif n == 5:
            lg.logging.info('Item number 5')
            course = input('Курс: ')
            lg.logging.info('User entered: {course}')
            group = input('Группа: ')
            lg.logging.info('User entered: {group}')
            name = input('Имя: ')
            lg.logging.info('User entered: {name}')
            surname = input('Фамилия: ')
            lg.logging.info('User entered: {surname}')
            date_of_birth = input('Дата рождения: ')
            lg.logging.info('User entered: {date_of_birth}')
            number = input('Номер телефона: ')
            lg.logging.info('User entered: {number}')
            email = input('Электронная почта: ')
            lg.logging.info('User entered: {email}')
            cr.create(course, group, name, surname, date_of_birth, number, email)

        elif n == 6:
            lg.logging.info('Item number 6')
            print('1. Поиск по фамилии')
            print('2. Поиск по группе.')
            print('3. Поиск по номеру телефона.')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logging.info('Item number 6.1')
                search = input('Фамилия: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(surname=search)
                user_id = input('id записи: ')
                lg.logging.info('User entered: {user_id}')

                new_course = input('Изменение курса: ')
                lg.logging.info('User entered: {new_course}')

                new_group = input('Изменение группы: ')
                lg.logging.info('User entered: {new_group}')

                new_date_of_birth = input('Изменение возраста: ')
                lg.logging.info('User entered: {new_date_of_birth}')

                new_number = input('Новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')

                cr.update(id=user_id, course=new_course, group=new_group, date_of_birth=new_date_of_birth, number=new_number)

            elif change == 2:
                lg.logging.info('item number 6.3')
                search = input('Номер телефона: ')
                lg.logging.info('User entered: {search}')

                cr.retrive(number=search)
                user_id = input('id записи: ')
                lg.logging.info('User entered: {user_id}')
                
                new_course = input('Изменение курса: ')
                lg.logging.info('User entered: {new_course}')

                new_group = input('Изменение группы: ')
                lg.logging.info('User entered: {new_group}')

                new_date_of_birth = input('Изменение возраста: ')
                lg.logging.info('User entered: {new_date_of_birth}')

                new_number = input('Новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')

                cr.update(id=user_id, course=new_course, group=new_group, date_of_birth=new_date_of_birth, number=new_number)

            else:
                lg.logging.info('Invalid menu value')
                print(
                    '\n Неправильно, введите повторно .')

        elif n == 7:
            lg.logging.info('Item number 7')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сhecking_the_number(input('Номер пункта: '))

            if deleting == 1:
                lg.logging.info('Item number 7.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('Item number 7.2')
                group = input('Введите группу: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(group=search))
                user_id = input('id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('Item number 7.3')
                search = input('Номер телефона: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            else:
                lg.logging.info('Invalid menu value')
                print(
                    '\nНеправильно, введите повторно')

        elif n == 8:
            lg.logging.info('End')
            print('Закрытие...')
            break

        else:
            lg.logging.info('Invalid menu value: {n}')
            print(
                '\nНеправильно, введите повторно')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('Invalid menu value: {arg}')
        print('\nНеправильно, введите повторно')
        arg = input('Выберите из меню: ')
    return int(arg)