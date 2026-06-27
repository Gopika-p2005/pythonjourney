credit_score =int(input("enter credit score.."))

if credit_score<=580 and credit_score>=300:
    print("pooor")
elif credit_score<=670 and credit_score>=580:
    print("fair")

elif credit_score<=740 and credit_score>=670:
    print("good")


elif credit_score<=800 and credit_score>=740:
    print("very good")


elif credit_score<=800 and credit_score>=850:
    print("excellent")
else:
    print("invalid credit score")
    