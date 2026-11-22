def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1

        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current

        print("Проход", i, ":", array)

    return array


array = list(map(int, input("Введите массив: ").split()))

print("Отсортированный массив:", insertion_sort(array))