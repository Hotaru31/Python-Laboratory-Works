m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

matrix = [list(map(int, input().split())) for _ in range(m)]

for j in range(n):
    column = [matrix[i][j] for i in range(m)]
    average = sum(column) / m

    count = sum(1 for x in column if x > average)

    print("Столбец", j + 1, ":", count)