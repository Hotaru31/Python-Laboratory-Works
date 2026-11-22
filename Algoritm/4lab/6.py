def reverse_words(words):
    if len(words) <= 1:
        return words

    return reverse_words(words[1:]) + [words[0]]


text = input("Введите предложение: ")
words = text.split()

print(" ".join(reverse_words(words)))