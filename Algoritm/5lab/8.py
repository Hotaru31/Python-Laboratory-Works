array = list(map(int, input("Введите массив: ").split()))

even_positions = array[1::2]

if even_positions:
    print("Минимальный элемент:", min(even_positions))
else:
    print("Нет элементов с чётными номерами")