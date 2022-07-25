# Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. 
# (1 - составное число)

import math

def inputNumber():
    num = int(input(f"Введите число: "))
    return num

def delitNum(n) :
    dividers = []
    a = 2
    while a * a < n + 1 :
        if n % a == 0 :
            dividers.append(a)
        while n % a == 0 :
            n //= a
        a += 1
    if n != 1 :
        dividers.append(n)
    return dividers 

def printNum (num):
    print(f"Cписок простых делителей числа: {num}")


delit = []
num = inputNumber()
delit = delitNum (num)
printNum (delit)

