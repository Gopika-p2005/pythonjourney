age = int(input("Enter age: "))

if age < 5:
    fare = 0
elif age <= 18:
    fare = 20
elif age <= 60:
    fare = 50
else:
    fare = 30

print("Fare:", fare)