p = float(input("Введите процент увеличения: "))

if 0 < p < 25:
    money = 1000
    months = 0

    while money <= 1100:
        money += money * p / 100
        months += 1

    print("Количество месяцев:", months)
    print("Итоговая сумма:", money)
else:
    print("Процент должен быть больше 0 и меньше 25")