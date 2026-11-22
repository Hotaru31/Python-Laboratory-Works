array = list(map(int, input("Введите массив: ").split()))

pairs = []

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            pairs.append((i + 1, j + 1))

if len(pairs) == 1:
    print("Номера элементов:", pairs[0])
else:
    print("В массиве нет ровно одной пары одинаковых элементов")