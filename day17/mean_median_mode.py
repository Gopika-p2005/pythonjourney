numbers=[10,11,12,7,8,9,10,11,15,10,10]

#mean
total=0
for num in numbers:

    total+=num

    mean=total/len(numbers)

print(mean)

#median

numbers.sort()

length=len(numbers)-1

mid=length//2

print(numbers[mid])

#numbers even aya number add 16

#mode

max_frequent_count=numbers.count(numbers[0])

max_frequent_number=numbers[0]

for num in numbers:

    if numbers.count(num) > max_frequent_count:

        max_frequent_count=numbers.count(num)

        max_frequent_number=num

print(max_frequent_number)
