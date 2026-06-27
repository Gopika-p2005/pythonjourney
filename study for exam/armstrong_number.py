num=153

number_copy=num

sum=0

count=0

while(num!=0):

    digit=num%10

    count+=1

    num=num//10

while(number_copy!=0):

    digit=number_copy%10

    expontial=digit**count

    sum+=expontial

    number_copy=number_copy//10

print(sum)