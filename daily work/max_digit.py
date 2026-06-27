def max_digit(num):

    largest=0

    while(num!=0):

        digit=num%10

        if digit>largest:

            largest=digit

        num=num//10

    print(largest)

max_digit(9573)
max_digit(3152)