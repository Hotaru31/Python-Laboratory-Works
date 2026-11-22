a = float(input("Введите первый элемент: "))
r = float(input("Введите знаменатель: "))
n = int(input("Введите количество элементов: "))

array = []

for i in range(n):
    array.append(a * r ** i)

print(array)