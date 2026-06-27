def calculate_bmi(height_in_cm,wight_in_kg):

    height_in_meter=height_in_cm /100

    bmi=wight_in_kg/ height_in_meter**2

    return bmi

print(calculate_bmi(175,75))