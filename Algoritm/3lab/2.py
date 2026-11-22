n = int(input("Введите N: "))

result = 1

for i in range(1, n + 1):
    result *= 1 + i / 10

print("Результат:", result)