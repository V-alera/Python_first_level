# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое 
# значение некоторой характеристики, и возвращает True, если это так. Если значение характеристики 
# для разных объектов отличается – то False. Для пустого набора объектов, функция должна возвращать 
# True. Аргумент characteristic – это функция, которая принимает объект и вычисляет его характеристику.

# values = [3, 6, 9, 12]

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

def same_by(characteristic, objects):
     if not objects:
         return True
     etalon = characteristic(objects[0])
     for obj in objects:
         if characteristic(obj)!=etalon:
             return False
     return True
 
n = inputNumber()
lst = inputValue(n)
print (f"Исходный список ", end=' ')
printlst(lst)
print()
print (f"Результат проверки на идентичность ", end=' ')
if same_by (lambda x: x % 2, lst):
    print("True")
else:
    print("False")