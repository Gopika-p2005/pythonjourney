amount=100000

withdrawal=int(input("enter a amount"))

if amount>withdrawal:

    print("sufficient balance")

    balance=amount-withdrawal
    
    print(balance)
else:

    print("insufficient balance")

