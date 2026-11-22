a = float(input("Введите A: "))
n = int(input("Введите N: "))

total = 1
power = 1

for i in range(1, n + 1):
    power *= a
    total += power

print("Сумма:", total)