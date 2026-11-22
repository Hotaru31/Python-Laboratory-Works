array = list(map(int, input("Введите массив: ").split()))

k = int(input("Введите K: "))
l = int(input("Введите L: "))

if 1 <= k <= l <= len(array):
    selected = array[k - 1:l]
    average = sum(selected) / len(selected)

    print("Среднее арифметическое:", average)
else:
    print("Некорректные K и L")