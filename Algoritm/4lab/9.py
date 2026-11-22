def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(source, "->", target)
        return

    hanoi(n - 1, source, auxiliary, target)
    print(source, "->", target)
    hanoi(n - 1, auxiliary, target, source)


n = int(input("Введите количество дисков (1–15): "))

if 1 <= n <= 15:
    hanoi(n, "A", "C", "B")
else:
    print("Допустимо от 1 до 15 дисков")