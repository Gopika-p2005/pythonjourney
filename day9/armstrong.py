number=int(input("enter number.."))

number_copy =number

sum=0

count=0

while(number!=0):

    digit=number%10

    count +=1

    number=number//10

while(number_copy!=0):

    digit=number_copy%10
    
    exponential=digit**count

    sum=sum+exponential

    number_copy=number_copy//10

print(sum) 