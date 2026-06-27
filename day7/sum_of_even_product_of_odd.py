"""
w.a.p display sum of even number and display product of odd number

"""




product =1

total = 0

for num in range(10,26):
    
    if num%2==0:

        total =total +num

    else:

        product = product*num 

print("even sum", total)

print("odd product",product)
