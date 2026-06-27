
salary =int(input("enter salary:"))


if salary<20000:

    bonus=(20/100)*salary

    print=(bonus)

elif salary>=20000 and salary<=50000:

    bonus=(10/100)*salary

    print(bonus)

elif salary>50000:

    bonus=(5/100)*salary

    print(bonus)

else:

    print("invalid")