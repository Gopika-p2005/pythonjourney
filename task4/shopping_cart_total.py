item=int(input("enter price.."))

total=0

user=input("shopping done..").lower

while(user!="done" and item!=0):

    total=total+item

    print(total)

    item=int(input("enter price.."))

    user=input("shopping done..").lower

print(total)
