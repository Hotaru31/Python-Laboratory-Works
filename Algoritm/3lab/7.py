a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a > 0 and b > 0 and a > b:
    remainder = a

    while remainder >= b:
        remainder -= b

    print("Остаток:", remainder)
else:
    print("Условия: A > B > 0")