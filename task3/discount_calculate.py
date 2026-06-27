amount=int(input("enter cash:"))

if amount<1000:

    discount=(5/100)*amount

    print(discount)


elif amount>=1000 and amount<5000:

    discount=(10/100)*amount

    print(discount)

elif amount>5000:

    discount=(15/100)*amount

    print(discount)

else:
    print("invalid")