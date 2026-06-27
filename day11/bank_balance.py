balance=10000

while(True):

    amount=int(input("enter amount you want to withdraw"))

    if amount>balance:

        print("insufficient balance")

        break

    balance=balance-amount


    print("your aval bal is",balance)