number=int(input("enter number.."))

sum=0

while(number!=0):

    last_digit=number%10

    cube = last_digit**3

    sum=cube+sum

    number=number//10
print(sum)