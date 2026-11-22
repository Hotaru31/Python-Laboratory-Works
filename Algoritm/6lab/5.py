m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

matrix = [list(map(int, input().split())) for _ in range(m)]

result = 0

for j in range(n):
    if all(matrix[i][j] % 2 != 0 for i in range(m)):
        result = j + 1
        break

print("Номер столбца:", result)