a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a != b:
    a = b = max(a, b)
else:
    a = b = 0

print("A =", a)
print("B =", b)