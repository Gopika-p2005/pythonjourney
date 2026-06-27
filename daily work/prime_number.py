def prime(num):

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break
    print(is_prime)

prime(9)
prime(27)
prime(7)