a = float(input("Введите A: "))
b = float(input("Введите B: "))
c = float(input("Введите C: "))

numbers = [a, b, c]
numbers.remove(min(numbers))

print("Сумма двух наибольших чисел:", sum(numbers))