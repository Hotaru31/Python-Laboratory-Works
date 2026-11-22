a = float(input("Введите координату A: "))
b = float(input("Введите координату B: "))
c = float(input("Введите координату C: "))

if min(a, b) <= c <= max(a, b):
    ac = abs(c - a)
    bc = abs(c - b)

    print("Произведение AC и BC:", ac * bc)
else:
    print("Точка C не находится между A и B.")