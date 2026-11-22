from collections import deque

queue = deque()

while True:
    print("\n1. Добавить элемент")
    print("2. Удалить элемент")
    print("3. Показать очередь")
    print("4. Проверить, пуста ли очередь")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        value = input("Введите элемент: ")
        queue.append(value)
        print("Элемент добавлен")

    elif choice == "2":
        if queue:
            print("Удален элемент:", queue.popleft())
        else:
            print("Очередь пуста")

    elif choice == "3":
        print("Очередь:", list(queue))

    elif choice == "4":
        if not queue:
            print("Очередь пуста")
        else:
            print("Очередь не пуста")

    elif choice == "0":
        print("Программа завершена")
        break

    else:
        print("Неверный выбор")