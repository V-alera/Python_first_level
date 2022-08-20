
database = {}
db = {'parents': 1, 'children': 2}

def reading_file_to_dict(number_file):
    with open (f'Homework_8.1/Denis/{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))
            print(database)

def print_childrens (second_name):
    id = [i[0] for i in database [db['parents']] if second_name in i][0]
    deti = [i for i in database [db['parents']] if id == i[1]]
    print(*[''.join(i[2:4]) + '\n' for i in deti])

reading_file_to_dict(1)
#reading_file_to_dict(2)
print(database)
print_childrens ('Иванов')