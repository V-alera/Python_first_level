# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 
# 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?

import random


sweets = 2021
max = 28
man1Sweets = 0
man2Sweets = 0
man1Num = 0
man2Num = 0
man1Flag = 0
man2Flag = 0

num = int(random.randrange(1, 6))
print (f"Загадано число от 0 до 5, кто угадывет тот стартует первым: ")

while man1Num != num or man2Num != num:
    man1Num = int(input(f"Игрок 1 ввел:  "))
    if man1Num == num: break
    man2Num = int(input(f"Игрок 2 ввел:  "))
    if man2Num == num: break

if man1Num == num:
    print (f"Игрок 1 выйграл жеребьевку, он начинает!")
    while sweets > 0:
        man1 = int(input(f"На столе лежит {sweets} конфет(а), очередь первого игрока взять не более {max}, взято:  "))
        man1Sweets += man1
        sweets -=man1
        if (sweets ==0): 
            print (f"Игрок 1 выйграл!!! Конфет не осталось")
            man1Flag = 1
            input()
            break

        else: 
            print (f"Конфет осталось {sweets}")
            man2 = int(input(f"На столе лежит {sweets} конфет(а), очередь второго игрока взять не более {max}, взято:  "))
            man2Sweets += man2
            sweets -=man2
        if (sweets ==0): 
            print (f"Игрок 2 выиграл!!! Конфет не осталось")
            man2Flag = 1
            input()
            break
        else: 
            print (f"Конфет осталось {sweets}")
            
elif man2Num == num: 
    print (f"Жеребьевку выйграл игрок 2, он начинает!")
    while sweets > 0:       
        man2 = int(input(f"На столе лежит {sweets} конфет(а), очередь второго игрока взять не более {max}, взято:  "))
        man2Sweets += man2
        sweets -=man2
        if (sweets ==0): 
            print (f"Игрок 2 выиграл!!! Конфет не осталось")
            man2Flag = 1
            input()
            break
        else: 
            print (f"Конфет осталось {sweets}")
            man1 = int(input(f"На столе лежит {sweets} конфет(а), очередь первого игрока взять не более {max}, взято:  "))
            man1Sweets += man1
            sweets -=man1
        if (sweets ==0): 
            print (f"Игрок 1 выиграл!!! Конфет не осталось")
            man1Flag = 1
            input()
            break
        else: 
            print (f"Конфет осталось {sweets}")

if man1Flag == 1: man1Sweets = man1Sweets + man2Sweets             
else: man2Sweets = man1Sweets + man2Sweets