array = list(map(int, input("Введите массив: ").split()))

result = []

left = 0
right = len(array) - 1

while left <= right:
    result.append(array[left])

    if left != right:
        result.append(array[right])

    left += 1
    right -= 1

print(result)