def my_long_word(n, text):
    return [word for word in text.split(' ') if (word) > n]

print(my_long_word(4, 'Bonjour, La terre et ronde ou plate ? '))