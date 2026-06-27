
even_total = 0

odd_total = 0

for num in range(5,11):

    if num%2==0:

        square = num ** 2

        even_total = even_total+square

    else:

        cube = num**3

        odd_total = odd_total+cube

print("even sum",even_total)

print("odd sum ",odd_total)