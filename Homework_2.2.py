# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. 
# Факториал 5! = 120

import math
import sys

def inputValue():
    num = int(input(f"Введите число N > 1: "))
    return num

def numSum(num):
    res = 1
    if num < 1: print ('Incorrect value, please try one more time')    
    else: 
        while num > 1: 
            res *= num
            num -=1

    return res

def printRes(res, num):
    print(f"Произведение чисел от 1 до {num} равно {res}")

number = None 

number = inputValue()

res = numSum(number)

printRes(res, number)