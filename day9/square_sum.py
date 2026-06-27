number=int(input("enter number.."))

sum=0

while(number!=0):

    last_digit=number%10

    square = last_digit**2

    sum=square+sum

    number=number//10
print(sum)