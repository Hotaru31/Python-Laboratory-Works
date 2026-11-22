m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

if m % 2 != 0 or n % 2 != 0:
    print("Количество строк и столбцов должно быть чётным")
else:
    matrix = [list(map(int, input().split())) for _ in range(m)]

    half_m = m // 2
    half_n = n // 2

    for i in range(half_m):
        for j in range(half_n):
            matrix[i][j], matrix[i + half_m][j + half_n] = (
                matrix[i + half_m][j + half_n],
                matrix[i][j]
            )

    for row in matrix:
        print(*row)