char = input("enter character").lower()

match char:
    case 'a'|'e'|'i'|'o'|'u':print("vowel")

    case _: print("consonant")