arr=[2,3,4,5,6]

target=11

for num in arr:

    difference=target-num

    if difference in arr:

        print(num,difference)