calories=[1200,1500,1700,1800,1900,2100,1900,2000]

#display all consumed calories

for cal in calories:

    print(cal)

print("==========================================")

#display calories>1500

for cal in calories:

    if cal>1500:

        print(cal)

print("===========================================")

#display calories < 1600

for cal in calories:

    if cal<1600:

        print(cal)

print("===========================================")

#display calories in range(1500,2000)

for cal in calories:

    if cal in range(1500,2001):

        print(cal)

print("===========================================")

#display total calories

sum=0

for cal in calories:

    sum=cal+sum

print(sum)

print("===========================================")

#display avg calorie

count=0

total=0

for cal in calories:

    count+=1

    total=cal+total

    avg=total/count

print(avg)