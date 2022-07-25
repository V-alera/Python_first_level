# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

import math

def inputNumber():
    num = int(input(f"Введите размер списка: "))
    return num

def inputValue(values):
    a = []
    for i in range(values):
        a.append(int(input(f"Введите числовое значение {i}: ")))
    return a

def printlst (list):
    print()
    print (lst)

def getUniqueValues (values):
    uniqueValues = []
    flag = 0
    j = 0
    values.sort()
    for i in values:
        if values.count(i) <= 1: uniqueValues.append(i)
    
    return uniqueValues

def printUniqueValues (r):
    print(f"Cписок неповторяющихся элементов исходной последовательности: {r}")

n = inputNumber()
lst = inputValue(n)
printlst (f"Исходный список имеет вид: {lst}")
res = getUniqueValues (lst)
printUniqueValues (res)
