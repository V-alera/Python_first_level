import csv
import os.path
import logger as lg


db_file_name = ''
db = []
global_id = 0

def initBase(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(course='', group='', name='', surname='', date_of_birth='', number='', email=''):
    global global_id
    global db
    global db_file_name
    if(course == ''):
        print("No course")
        return
    if(group == ''):
        print("No group")
        return
    if(name == ''):
        print("No name")
        return
    if(surname == ''):
        print("No surname")
        return
    if(date_of_birth == ''):
        print("No date of birth")
        return
    if(number == ''):
        print("No telephone")
        return
    if(email == ''):
        print("No E-mail")
        return

    for row in db:
        if(row[1] == course.title() and row[2] == group.title() and row[3] == name.title() and row[4] == surname.title() and row[5] == date_of_birth.title() and row[6] == number and row[7] == email.lower()):
            print("Info is already exist")
            return

    global_id += 1
    new_row = [str(global_id), course.title(), group.title(), name.title(),
               surname.title(), date_of_birth.title(), number, email.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrive(id='', course='', group='', name='', surname='', date_of_birth='', number='', email=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(course != '' and row[1] != course.title()):
            continue
        if(group != '' and row[2] != group.title()):
            continue
        if(name != '' and row[3] != name.title()):
            continue
        if(surname != '' and row[4] != surname.title()):
            continue
        if(date_of_birth != '' and row[5] != date_of_birth.title()):
            continue
        if(number != '' and row[6] != number):
            continue
        if(email != '' and row[7] != email.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'No info'
    else:
        return result


def update(id='', new_course='', new_group='', new_name='', new_surname='', new_date_of_birth='', new_number='', new_email=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('update id')
        return
    with open(db_file_name, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                
                if(new_course != ''):
                    row[1] = new_course.title()

                if(new_group != ''):
                    row[2] = new_group.title()

                if(new_name != ''):
                    row[3] = new_name.title()

                if(new_surname != ''):
                    row[4] = new_surname.title()

                if(new_date_of_birth != ''):
                    row[5] = new_date_of_birth.title()

                if(new_number != ''):
                    row[6] = new_number

                if(new_email != ''):
                    row[7] = new_email.lower()

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('delete id')
        return


    for row in db:
        if (row[0] == id):
            db.remove(row)
            break


    with open(db_file_name, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def get_token():
    file = open('token.csv', 'r')
    for i in file:
        token = i
    file.close()
    return token