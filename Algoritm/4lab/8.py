def count_digits(n):
    n = abs(n)

    if n < 10:
        return 1

    return 1 + count_digits(n // 10)


n = int(input("Введите число: "))

print("Количество цифр:", count_digits(n))