# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите день недели')
num = int(input())
if (num > 0 and num < 6) : print(num, '-> no')
elif (num > 5 and num < 8) : print(num, '-> yes')
else : print('Incorrect value, please try one more time')