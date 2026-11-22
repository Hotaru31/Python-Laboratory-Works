n = int(input("Введите N: "))
a = int(input("Введите первый элемент: "))
b = int(input("Введите второй элемент: "))

array = [a, b]

for i in range(2, n):
    array.append(sum(array))

print(array[:n])