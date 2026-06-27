char = input("enter character")

if char.isalpha():

    print("ALPHABET")

elif char.isdigit():
    print("NUMBER")

elif not char.isalnum ():

    print("SPECIAL CHARACTER")