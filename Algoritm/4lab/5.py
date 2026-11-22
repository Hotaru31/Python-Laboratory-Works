def binary_search(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if array[middle] == target:
        return middle

    if array[middle] < target:
        return binary_search(array, target, middle + 1, right)

    return binary_search(array, target, left, middle - 1)


array = list(map(int, input("Введите отсортированный массив: ").split()))
target = int(input("Введите искомое число: "))

result = binary_search(array, target, 0, len(array) - 1)

print("Индекс:", result)