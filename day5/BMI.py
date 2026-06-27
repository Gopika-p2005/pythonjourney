"""
height_in_cm
weight_in_kg

bmi=weight_in_kg / (height_in_meter^2)

"""

height_in_cm = int(input("enter height in cm.."))

weight_in_kg = int(input("enter weight in kg.."))

height_in_meter = height_in_cm /100

bmi = weight_in_kg/(height_in_meter**2)

bmi=round(bmi)

print(bmi)

if bmi<19:
    print("underweight")

elif bmi in range(19,25):
    print("healty weight")

elif bmi in range(25,30):
    print("overweight")

else:
    print("obese")