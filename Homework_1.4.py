# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

import math


def inputValue():
    part = int(input(f"Введите значение четверти: "))
    return part

def checkPart(num):
    if (num == 1): print (f"x > 0, y > 0")
    elif (num == 2): print (f"x > 0, y < 0")
    elif (num == 3): print (f"x < 0, y < 0")
    else: print (f"x < 0, y > 0")

partValue = None

partValue = inputValue()

checkPart(partValue)