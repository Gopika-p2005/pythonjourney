
num1=123

num2=456

smallest_num=num1 if num1<num2 else num2

for i in range(1,smallest_num+1):
          
    if num1%i==0 and num2%i==0:

        print(i)

