n = int(input("Введите число от 10 до 40: "))

if 10 <= n <= 40:
    last_two = n % 100
    last = n % 10

    if 11 <= last_two <= 14:
        word = "заданий"
    elif last == 1:
        word = "учебное задание"
    elif 2 <= last <= 4:
        word = "учебных задания"
    else:
        word = "учебных заданий"

    print(n, word)
else:
    print("Число должно быть от 10 до 40")