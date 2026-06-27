number=int(input("enter number.."))

small=number%10

large =0

#smallest_digit=1

while(number!=0):

    digit=number%10

    if digit>large :

        large=digit

    
    if digit<large:
        
        small=digit
        
    number=number//10

print("smallest",small)

print("largest",large)
