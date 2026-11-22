a = float(input("Введите A: "))
b = float(input("Введите B: "))
c = float(input("Введите C: "))

if abs(a - b) < abs(a - c):
    print("Точка B ближе к A")
    print("Расстояние:", abs(a - b))
else:
    print("Точка C ближе к A")
    print("Расстояние:", abs(a - c))