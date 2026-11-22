array = list(map(int, input("Введите массив: ").split()))

odd_positions = array[0::2]
even_positions = array[1::2][::-1]

result = odd_positions + even_positions

print(result)