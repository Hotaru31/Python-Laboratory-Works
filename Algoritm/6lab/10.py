n = int(input("Введите размер квадратной матрицы: "))

matrix = [list(map(int, input().split())) for _ in range(n)]

print("Суммы диагоналей:")

for start_col in range(n - 1, -1, -1):
    total = 0
    i = 0
    j = start_col

    while i < n and j < n:
        total += matrix[i][j]
        i += 1
        j += 1

    print(total)

for start_row in range(1, n):
    total = 0
    i = start_row
    j = 0

    while i < n and j < n:
        total += matrix[i][j]
        i += 1
        j += 1

    print(total)