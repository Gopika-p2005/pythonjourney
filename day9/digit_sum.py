number=int(input("enter number.."))

sum=0

while(number!=0):

    last_digit=number%10

    sum=last_digit+sum

    number=number//10
print(sum)