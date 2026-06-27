total = 0

while True:
    price = float(input("Enter product price: "))
    total += price

    choice = input("Add more products? (yes/no): ")

    if choice.lower() == "no":
        break

print("Final Bill:", total)