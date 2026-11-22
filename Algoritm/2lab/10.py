year = int(input("Введите год: "))

animals = [
    "Крыса", "Бык", "Тигр", "Кролик",
    "Дракон", "Змея", "Лошадь", "Коза",
    "Обезьяна", "Петух", "Собака", "Свинья"
]

colors = ["зеленый", "красный", "желтый", "белый", "черный"]

if year >= 1984:
    delta = year - 1984
else:
    delta = (year - 1984) % 60

animal = animals[delta % 12]
color = colors[(delta // 2) % 5]

print(color.capitalize(), animal)