nums=[11,12,13,11,14,15,11]

num_dict={}

for num in nums:

    num_dict[num]=nums.count(num)

for k,v in num_dict.items():

    if v>1:

        print(k)