# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть 
# копеек отбрасывается.Требуется определить: через сколько лет вклад составит не менее Y рублей.

def inputValue():
    x = int(input(f"Введите значение вклада X = "))
    p = int(input(f"Введите значение процентов по вкладу P = "))
    y = int(input(f"Введите значение желаемого значения вклада Y = "))
    return x, p, y

def getResult(x, p, y):
    num = 0
    while x < y:
        x += int(x / 100 * p)
        num += 1
    return num

def printRes(Years, money):    
    print(f"Через {Years} лет вклад составит {money} rub")

a, b, c = inputValue()
numYears = getResult(a, b, c)
printRes(numYears, c)