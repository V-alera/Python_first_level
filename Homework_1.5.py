# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
from tokenize import Double


def inputValue():
    x1 = float(input(f"Введите значение x1: "))
    x2 = float(input(f"Введите значение x2: "))
    y1 = float(input(f"Введите значение y1: "))
    y2 = float(input(f"Введите значение y2: "))
    return x1, x2, y1, y2

def pointInterval(x1, x2, y1, y2):
    res = ((y1 - x1) ** 2 + (y2 - x2) ** 2) ** (0.5)
    return res

def printRes(res):
    print(f"Длина отрезка {res}")

x1 = None 
x2 = None 
y1 = None 
y2 = None 
res = None

x1, x2, y1, y2  = inputValue()

res = pointInterval(x1, x2, y1, y2)

printRes(res)