# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""

import random


sweets = 2021
max = 28
manSweets = 0
computerSweets = 0

num = int(random.randrange(1, 6))
print (f"Загадано число от 0 до 5, кто угадывет тот стартует первым: ")

manNum = 0
compNum = 0

while manNum != num or compNum != num:
    man = int(input(f"Человек ввел:  "))
    if manNum == num:
        print (f"Человек выйграл жеребьевку, он начинает!")
        while sweets > 0:
            man = int(input(f"На столе лежит {sweets}, очередь человека взять не более {max}, взято:  "))
            manSweets += man
            sweets -=man
            if (sweets ==0): 
                print (f"Человек выиграл!!! Конфет не осталось")
                input()
                break
            else: print (f"Конфет осталось {sweets}")
            computer = int(random.randrange(1, 29))
            print(f"На столе лежит {sweets}, компьютер взял:  {computer}")
            computerSweets += computer
            sweets -=computer
            if (sweets ==0): 
                print (f"Компьютер выиграл!!! Конфет не осталось")
                input()
                break
            else: print (f"Конфет осталось {sweets}")
        quit()
    else: 
        print (f"Жеребьевку выйграл компьютер, он начинает!")
        while sweets > 0:
            computer = int(random.randrange(1, 29))
            print(f"На столе лежит {sweets}, компьютер взял:  {computer}")
            computerSweets += computer
            sweets -=computer
            if (sweets ==0): 
                print (f"Компьютер выиграл!!! Конфет не осталось")
                input()
                break
            else: print (f"Конфет осталось {sweets}")
            man = int(input(f"На столе лежит {sweets}, очередь человека взять не более {max}, взято:  "))
            manSweets += man
            sweets -=man
            if (sweets ==0): 
                print (f"Человек выиграл!!! Конфет не осталось")
                input()
                break
            else: 
                print (f"Конфет осталось {sweets}")
        quit()
