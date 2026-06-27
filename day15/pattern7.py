for row in range(1,7):

    for col in range(1,7):

        if row==1 or row==6 or col==1 or col==6 or row==col or row+col==7:

            print("*",end="\t")

        else:

            print(end="\t")

    print()