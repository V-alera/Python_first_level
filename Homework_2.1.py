# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11



import math
import sys

def inputValue():
    num = float(input(f"Введите число количеством цифр не более 15: "))
    return num

def numSum(num):
    sum = 0
    num = num*1000000000000000
    if num < 0: print ('Incorrect value, please try one more time, the quantity of numbers is more than 50')    
    else: 
        while num > 0: 
            sum = int(sum + num % 10)
            num = int(num / 10)

    return sum

def printRes(res):
    print(f"Сумма цифр числа равна {res}")

number = None 

number = inputValue()

res = numSum(number)

printRes(res)