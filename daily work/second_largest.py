num=653

second=0

largest=0

while(num!=0):

    digit=num%10

    if digit>largest:

        second=largest

        largest=digit

    elif digit>second and digit!=largest:

        second=digit

    num=num//10

print(second)