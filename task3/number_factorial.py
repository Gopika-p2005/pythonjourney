number = int(input("enter number.."))

fact =1

for num in range(1,number+1):

    fact=fact*num


print(f"factorial of {number}! = {fact}")