def decompose(n, start=2):
    if n == 0:
        return []

    for p in range(start, n + 1):
        if is_prime(p):
            result = decompose(n - p, p)

            if result is not None:
                return [p] + result

    return None


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input("Введите число: "))

if n >= 2:
    result = decompose(n)
    print("Разложение:", " + ".join(map(str, result)))
else:
    print("Число должно быть не меньше 2")