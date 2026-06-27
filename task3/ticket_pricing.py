age=int(input("enter age.."))
day=input("enter day(weekend/weekday):")

if age<12:
    price=100

elif age<=60:
    price=200

else:
    price=150

if day.lower()=="weekend":

    price+=50


print("ticket price",price)