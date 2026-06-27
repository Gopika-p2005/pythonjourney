km=int(input("enter distance.."))

if km<=5:
    fare = km*5

elif km<=10:
    fare= (5*10)+(km-5)*8

else:
    fare=(5*10)+(5*8)+(km-10)*5


print("fare",fare)