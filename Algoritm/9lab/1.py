def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

        print("Шаг", i + 1, ":", array)

    return array


array = list(map(int, input("Введите массив: ").split()))

print("Отсортированный массив:", selection_sort(array))