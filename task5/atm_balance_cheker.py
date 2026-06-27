balance=10000
def deposite(amount):
    global balance
    balance=balance+amount

    print(balance)


def withdrowal(cash):
    global balance

    if cash>balance:

        print("insuffient balance")

    else:

        print(balance-cash)

deposite(500)
withdrowal(1000)   

       