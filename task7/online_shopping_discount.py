purchase_amount=int(input("enter amount"))

if purchase_amount<2000:

    discount=(5/100)*purchase_amount

    print(purchase_amount-discount)

elif purchase_amount<3000:

    discount=(10/100)*purchase_amount

    print(purchase_amount-discount)

elif purchase_amount>=3000:

    discount=(15/100)*purchase_amount

    print(purchase_amount-discount)