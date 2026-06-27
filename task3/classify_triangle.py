first_side =int(input("enter first side.."))

second_side =int(input("enter second side.."))

third_side =int(input("enter third side.."))

if first_side==second_side==third_side:

    print("Eqilateral")

elif first_side==second_side or first_side==third_side or second_side==third_side:

    print("isosceles")

else:


    print("scalene")