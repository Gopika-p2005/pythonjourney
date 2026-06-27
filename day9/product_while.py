number=int(input("enter number.."))

product=1

while(number!=0):

    last_digit=number%10

    product=last_digit*product

    number=number//10
print(product)