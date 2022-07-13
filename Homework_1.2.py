# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех 
# значений предикат.

def inputValue(values):
    XYZ = ["X", "Y", "Z"]
    a = []
    for i in range(values):
        a.append(input(f"Введите значение {XYZ[i]}: "))
    return a


def checkPredicate(arr):
    left = not (arr[0] or arr[1] or arr[2])
    right = not arr[0] and not arr[1] and not arr[2]
    result = left == right
    return result


mass = inputValue(3)

if checkPredicate(mass) == True: print(f"Утверждение истинно")
else: print(f"Утверждение ложно")

