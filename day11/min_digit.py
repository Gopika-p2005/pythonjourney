def min_digit(number):


    result = number%10


    while(number!=0):

        digit=number%10

        if digit<result:

            result=digit

        number=number//10

    return result


print(min_digit(123))
print(min_digit(234))
print(min_digit(345))