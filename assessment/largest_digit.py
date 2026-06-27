number=int(input("enter number.."))

largest_digit=0

while(number!=0):

    digit=number%10

    if digit>largest_digit:

        largest_digit=digit

    number=number//10
print("enter largest",largest_digit)