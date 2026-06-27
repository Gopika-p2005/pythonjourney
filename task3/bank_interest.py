age = int(input("enter age.."))

if age<18:
    rate=4

elif age<=60:
    rate=6

else:
    rate=8

print("interest rate:",rate,"%")