# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141


pi = 0
sign = 1
d = 10

num0 = int(input(f"Введите точность числа Pi: "))
num = num0 + 1
for i in range (1, num):
    d *= 10
d = d + 1

for i in range (1, d, 2):
    pi += sign*4 / i
    sign *= -1

print (f"Число Пи с заданной точностью {num0} имеет вид {round (pi, num0)}")
