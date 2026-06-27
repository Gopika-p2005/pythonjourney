arr=[2,3,4,5,6,7]

target=11

length=len(arr)-1

for i in range(0,length):

    for j in range(i+1,length+1):

        cur_sum=arr[i]+arr[j]

        if cur_sum==target:

            print(arr[i],arr[j])