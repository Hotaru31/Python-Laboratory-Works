array = list(map(int, input("Введите массив: ").split()))

if len(array) < 2:
    print("Разность:", 0)
else:
    difference = array[1] - array[0]

    for i in range(1, len(array)):
        if array[i] - array[i - 1] != difference:
            difference = 0
            break

    print("Разность:", difference)