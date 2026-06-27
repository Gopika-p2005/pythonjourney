number=int(input("enter number.."))

smallest_digit=number%10

#smallest_digit=1

while(number!=0):

    digit=number%10

    if digit<smallest_digit:

        smallest_digit=digit

    number=number//10
print("smallest",smallest_digit)
