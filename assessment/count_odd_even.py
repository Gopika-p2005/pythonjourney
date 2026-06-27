even_count,odd_count=0,0

limit=int(input("enter lilmit.."))


for num in range(1,limit+1):

    if num%2==0:

        even_count+=1

    else:

        odd_count+=1


print("odd count",odd_count)

print("even count",even_count)