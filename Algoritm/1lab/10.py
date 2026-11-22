from math import sqrt

x1, y1 = map(float, input("Введите координаты A: ").split())
x2, y2 = map(float, input("Введите координаты B: ").split())
x3, y3 = map(float, input("Введите координаты C: ").split())

a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

p = a + b + c
half_p = p / 2

area = sqrt(half_p * (half_p - a) *
            (half_p - b) * (half_p - c))

print("Периметр:", p)
print("Площадь:", area)