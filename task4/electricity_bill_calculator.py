units =int(input("enter units.."))

while(units!=0):

    if units<=100:

        bill=units*5

    elif units<=200:

        bill=units*7

    else:
        bill=units*10


    print("bill amount",bill)

    units=int(input("enter units.."))