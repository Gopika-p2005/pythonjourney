nums=[10,11,12,11,13,14,15]

num_dict={}

for num in nums:

    num_dict[num]=nums.count(num)

for k,v in num_dict.items():

    if v>1:
        print(k)    
