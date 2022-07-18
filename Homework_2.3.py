# Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение 
# второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, 
# если из последовательности удалить наибольший элемент.

def inputValue(values):
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
    a = []
    for i in range(values):
        a.append(int(input(f"Number {num[i]}:   ")))
    return a

def listSort(values):
    values.sort()
    return values

def printValues(values):
    print(f"Сортированный список: {values}")

def printResult(values, number):
    print(f"Второе по значению число {values[number-2]}")


print(f"Введите 10 любых чисел")

listValues = inputValue(10)
listSort(listValues)
printValues(listValues)

printResult(listValues, 10)