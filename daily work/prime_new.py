def is_prime(num):

    prime=True

    for i in range(2,num):

        if num%i==0:

            prime=False
    print(prime)

is_prime(9)
is_prime(7)