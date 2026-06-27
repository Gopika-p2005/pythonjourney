arr=[2,3,4,5]

target=8

for num in arr:

    difference=target-num

    if difference in arr and difference!=num:

        print(difference,num)
