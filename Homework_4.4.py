# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import math

def inputNumber():
    num = int(input(f"Введите степень k: "))
    lastK = int(input(f"последний коэффициент многочлена: "))
    return num, lastK

def inputValue(values):
    a = []
    for i in range(values):
        a.append(int(input(f"Введите коэффициенты многочлена {i}:   ")))
    return a

def printPolynom(pol, num, l):
    print(f"A(x) = ", end=' ') 
    for i in pol:
        if num==0: 
            print(f"+ {pol[-1]} +", end=' ')
            break

        else: 
            print(f"{i}x**{num} +", end=' ')
            num -=1
    print(f"{l}", end=' ') 

n, lastK = inputNumber()
lst = inputValue(n)
print(f"Многочлен имеет вид: ", end=' ')
printPolynom(lst, n, lastK)