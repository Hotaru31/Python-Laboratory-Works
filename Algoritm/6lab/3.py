m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

matrix = [list(map(int, input().split())) for _ in range(m)]

products = []

for j in range(n):
    product = 1

    for i in range(m):
        product *= matrix[i][j]

    products.append(product)

minimum = min(products)

print("Номер столбца:", products.index(minimum) + 1)
print("Минимальное произведение:", minimum)