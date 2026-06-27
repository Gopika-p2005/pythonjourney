total = 0

while(True):
    price = int(input("Enter item price: "))
    total += price

    choice = input("Add more items? (yes/no): ")

    if choice== "no":
        break

print("Total Bill:", total)