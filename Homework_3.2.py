# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

def inputNumber():
    num = int(input(f"Введите размер списка: "))
    return num


def inputValue(values):
    a = []
    for i in range(values):
        a.append(int(input(f"Введите значение {i}: ")))
    return a

def printlst (list):
    print()
    print (lst)

def multiNumbers(List):
    a = []
    step = 0
    countBack = len(List)-1
    flag = math.trunc((len(List)-1)/2)
    for number in range(len(List)):
        if countBack%2 == 0 and number==countBack: 
            a.append(List[number])
            break
        if (flag == step - 1): break
        else: a.append(List[number]*List[countBack])
        countBack = countBack - 1
        step = step + 1
            
    return a

sumL = 0
n = inputNumber()
lst = inputValue(n)
printlst (lst)
print('Произведение чисел - ', multiNumbers(lst))
