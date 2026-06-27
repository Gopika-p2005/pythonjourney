arr=[2,3,4,5,6,7,8]

target=11

arr.sort()

left=0

right=len(arr)-1

while(left<right):

    cur_sum=arr[left]+arr[right]

    if cur_sum==target:

        print(arr[left],arr[right])

        left+=1

        right-=1

    elif cur_sum<target:

        left+=1

    elif cur_sum>target:

        right-=1