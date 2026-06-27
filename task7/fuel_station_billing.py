fuel = input("Enter fuel type (petrol/diesel): ")
qty = float(input("Enter quantity: "))

if fuel.lower() == "petrol":
    amount = qty * 100
elif fuel.lower() == "diesel":
    amount = qty * 90
else:
    amount = 0

print("Total Amount:", amount)