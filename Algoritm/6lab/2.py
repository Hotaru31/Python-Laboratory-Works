m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

k = int(input("Введите номер строки K: "))

if 1 <= k <= m:
    row = matrix[k - 1]

    total = sum(row)
    product = 1

    for x in row:
        product *= x

    print("Сумма:", total)
    print("Произведение:", product)
else:
    print("Некорректный номер строки")