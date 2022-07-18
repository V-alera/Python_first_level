# Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение 
# второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, 
# если из последовательности удалить наибольший элемент.

def inputValue(values):
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
    a = []
    for i in range(values):
        a.append(int(input(f"Number {num[i]}:   ")))
    return a

def listFind(values):
    max1 = values[0]
    max2 = 0
    i = 0
    while (i < len(values)):
        if max1 < values[i]: max2 = max1
        max1 = values[i]
        i = i + 1
    return max2

def printResult(number):
    print(f"Второе по значению число {number}")


print(f"Введите 10 любых чисел")

listValues = inputValue(10)
maxSecondValue = listFind(listValues)

printResult(maxSecondValue)