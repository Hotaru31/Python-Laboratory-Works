array = list(map(int, input("Введите массив: ").split()))

result = 0

for i in range(len(array)):
    if i == 0:
        if len(array) > 1 and array[i] > array[i + 1]:
            result = i + 1
    elif i == len(array) - 1:
        if array[i] > array[i - 1]:
            result = i + 1
    else:
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            result = i + 1

print("Номер последнего локального максимума:", result)