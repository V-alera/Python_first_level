# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Переменная transformation должна быть глобальной, чтобы проверяющая ее система смогла ее найти. 
# Кроме transformation Вам ничего не надо писать, в т.ч. печать на экран.


transformation = lambda x: x.copy()

transformed_values = lambda x: map(transformation, x)

def inputNumber():
    num = int(input(f"Введите размер списка: "))
    return num

def inputValue(values):
    a = []
    for i in range(values):
        a.append(int(input(f"Введите значение {i}: ")))
    return a

def printlst (list):
    print(lst)

n = inputNumber()
lst = inputValue(n)
print (f"Исходный список ", end=' ')
printlst (lst)
newLst = transformed_values(lst)
print (f"Новый список transformation", end=' ')
printlst (newLst)