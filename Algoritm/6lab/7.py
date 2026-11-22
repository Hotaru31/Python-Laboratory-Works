m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

matrix = [list(map(int, input().split())) for _ in range(m)]

minimum = min(min(row) for row in matrix)
maximum = max(max(row) for row in matrix)

min_column = max_column = 0

for i in range(m):
    for j in range(n):
        if matrix[i][j] == minimum:
            min_column = j
        if matrix[i][j] == maximum:
            max_column = j

for i in range(m):
    matrix[i][min_column], matrix[i][max_column] = (
        matrix[i][max_column],
        matrix[i][min_column]
    )

for row in matrix:
    print(*row)