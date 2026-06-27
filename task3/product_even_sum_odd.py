product=1

total=0

for num in range(10,21):

    if num%2==0:

        product=product*num

    else:

        total=total+num


print("even product",product)

print("odd sum ",total)