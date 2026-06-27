mark1 = int(input("enter mark1"))
mark2 = int(input("enter mark2"))
mark3 = int(input("enter mark3"))

avg = (mark1+mark2+mark3)/3
if mark1<40 or mark2<40 or mark3<40:

    print("fail")

elif avg>=75:

    print("distinction")

elif avg>=60:
    print("first class")

else:
    print("pass")