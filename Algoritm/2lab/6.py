n = int(input("Введите число от 1 до 999: "))

if 1 <= n <= 999:
    if n % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    if n < 10:
        length = "однозначное"
    elif n < 100:
        length = "двузначное"
    else:
        length = "трехзначное"

    print(parity, length, "число")
else:
    print("Число должно быть от 1 до 999")