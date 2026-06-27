num=int(input("enter number.."))

first=0

second=1

count=0

while(count!=(num-1)):
    sum=first+second

    first=second

    second=sum

    count+=1

print(sum)