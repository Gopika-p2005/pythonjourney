token = 1

while True:
    name = input("Enter patient name (or exit): ")

    if name.lower() == "exit":
        break

    print("Token Number:", token)
    token += 1