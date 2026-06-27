balance=1000

while(balance>0):

    amount=int(input("enter withdrawal amounnt.."))


    if amount==0:

        break
    elif amount<=balance:

        balance-=amount

        print(balance)