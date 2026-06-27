def is_prime(num):

    result = True


    for i in range(2,num):


        if num%i==0:


            result=False

            break


    return result

print(is_prime(5))
print(is_prime(12))