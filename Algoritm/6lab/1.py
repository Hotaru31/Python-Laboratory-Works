n = int(input("Введите нечётный размер матрицы: "))

if n % 2 == 0 or n < 1:
    print("Размер должен быть нечётным")
else:
    matrix = [[0] * n for _ in range(n)]
    value = 1

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while left <= right and top <= bottom:
        for i in range(top, bottom + 1):
            matrix[i][left] = value
            value += 1
        left += 1

        for j in range(left, right + 1):
            matrix[bottom][j] = value
            value += 1
        bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][right] = value
                value += 1
            right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[top][j] = value
                value += 1
            top += 1

    for row in matrix:
        print(*row)