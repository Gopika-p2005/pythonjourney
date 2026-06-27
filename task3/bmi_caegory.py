bmi =int(input("enter bmi.."))

if bmi<18.5:
    print("underweight")

elif bmi<25:
    print("normal")

elif bmi<30:
    print("overweight")

else:
    print("obese")