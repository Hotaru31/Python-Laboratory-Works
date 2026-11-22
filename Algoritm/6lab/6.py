m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

matrix = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    min_index = matrix[i].index(min(matrix[i]))
    max_index = matrix[i].index(max(matrix[i]))

    matrix[i][min_index], matrix[i][max_index] = (
        matrix[i][max_index],
        matrix[i][min_index]
    )

for row in matrix:
    print(*row)