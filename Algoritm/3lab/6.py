a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a < b:
    for number in range(a, b + 1):
        for i in range(number):
            print(number, end=" ")
        print()
else:
    print("A должно быть меньше B")