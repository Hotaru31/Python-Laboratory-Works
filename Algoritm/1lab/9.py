x1 = float(input("Введите x первой вершины: "))
y1 = float(input("Введите y первой вершины: "))

x2 = float(input("Введите x противоположной вершины: "))
y2 = float(input("Введите y противоположной вершины: "))

a = abs(x2 - x1)
b = abs(y2 - y1)

perimeter = 2 * (a + b)
area = a * b

print("Периметр:", perimeter)
print("Площадь:", area)