# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def inputNumber():
    num = int(input(f"Введите размер списка: "))
    return num


def inputValue(values):
    a = []
    for i in range(values):
        a.append(int(input(f"Введите значение {i}: ")))
    return a

def printlst (list):
    print()
    print (lst)

def SumOfOddNumbers(List):
    sum = 0
    count = 0
    for number in List:
        if count % 2 != 0:
            sum += number
        count = count + 1
    return sum

sumL = 0
n = inputNumber()
lst = inputValue(n)
printlst (lst)
print('Сумма нечетных чисел - ', SumOfOddNumbers(lst))
