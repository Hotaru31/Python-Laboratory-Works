n = int(input("Введите число: "))

if n > 0:
    print("Положительное")
elif n < 0:
    print("Отрицательное")
else:
    print("Нулевое")

if n != 0:
    if n % 2 == 0:
        print("Четное")
    else:
        print("Нечетное")