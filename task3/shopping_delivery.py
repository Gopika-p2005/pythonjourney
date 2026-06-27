amount= int(input("enter order amount.."))


if amount>2000:
    delivery=0

elif amount>=1000:

    delivery=50

else:
    delivery=100

print(" delivery charge",delivery)