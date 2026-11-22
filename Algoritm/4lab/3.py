def power(a, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / power(a, -n)

    return a * power(a, n - 1)


a = float(input("Введите основание: "))
n = int(input("Введите степень: "))

if a == 0 and n < 0:
    print("Нельзя возвести ноль в отрицательную степень")
else:
    print("Результат:", power(a, n))