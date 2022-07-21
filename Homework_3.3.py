# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

def inputNumber():
    num = int(input(f"Введите размер списка: "))
    return num


def inputValue(values):
    a = []
    for i in range(values):
        a.append(float(input(f"Введите значение {i}: ")))
    return a

def changeValues(values):
    a = []
    for i in range(len(values)):
        a.append(values[i] - int(values[i]))
    return a

def printDiff(max, min):
    print (f"Разница между максимальной дробной часть и минимальной равна {round((max - min), 5)}")

num = inputNumber()
lst = inputValue(num)
newLst = changeValues(lst)
maxNumber = max(newLst)
minNumber = min(newLst)
printDiff(maxNumber, minNumber)