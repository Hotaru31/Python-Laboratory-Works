
def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        print("Проверяем элемент:", array[middle])

        if array[middle] == target:
            return middle

        elif array[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


array = list(map(int, input("Введите отсортированный массив: ").split()))
target = int(input("Введите искомое число: "))

result = binary_search(array, target)

if result != -1:
    print("Элемент найден. Индекс:", result)
else:
    print("Элемент не найден")