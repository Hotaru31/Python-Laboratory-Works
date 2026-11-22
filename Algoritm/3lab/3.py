n = int(input("Введите N: "))

total = 0

for i in range(1, n + 1):
    total += 2 * i - 1
    print("После", i, "слагаемого:", total)

print("Квадрат числа:", total)