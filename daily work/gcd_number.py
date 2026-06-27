def number(num1,num2):

    gcd=1

    smallest_num=min(num1,num2)

    for i in range(1,smallest_num+1):

        if num1%i==0 and num2%i==0:

            gcd=i

    print(gcd)


number(12,13)