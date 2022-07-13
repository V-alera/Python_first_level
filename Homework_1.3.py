# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def inputValue(values):
    XY = ["X", "Y"]
    a = []
    for i in range(values):
        a.append(int(input(f"Введите значение {XY[i]}: ")))
    return a

def checkPart(arr):
    if (arr[0] > 0 and arr[1] > 0): result = 1
    elif (arr[0] > 0 and arr[1] < 0): result = 2
    elif (arr[0] < 0 and arr[1] < 0): result = 3
    elif (arr[0] < 0 and arr[1] > 0): result = 4
    else: print(f"One of coordinates lies on the border")
    return result

mass = inputValue(2)

if checkPart(mass) > 0: print(f"x={mass[0]} y={mass[1]} -> {checkPart(mass)}")
else: print ("Одно из значений равняется нулю")