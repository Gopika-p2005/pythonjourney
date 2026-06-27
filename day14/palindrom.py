def is_palindrom(word):

    reversed_word=word[::-1]

    return word==reversed_word

print(is_palindrom("madam"))
print(is_palindrom("dam"))