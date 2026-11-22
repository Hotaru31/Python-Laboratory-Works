m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

matrix = [list(map(int, input().split())) for _ in range(m)]

matrix.sort(key=lambda row: row[0])

for row in matrix:
    print(*row)