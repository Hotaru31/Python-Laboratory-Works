def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input("Введите число: "))

if n >= 0:
    print("Факториал:", factorial(n))
else:
    print("Число должно быть неотрицательным")