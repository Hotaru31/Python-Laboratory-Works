def is_palindrome(text):
    text = "".join(c.lower() for c in text if c.isalnum())

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


word = input("Введите строку: ")

if is_palindrome(word):
    print("Это палиндром")
else:
    print("Это не палиндром")