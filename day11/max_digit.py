def max_digit(number):

    result=0

    while(number!=0):

        last_digit=number%10

        if last_digit>result:

            result=last_digit

        number=number//10

    return result


print(max_digit(234))
