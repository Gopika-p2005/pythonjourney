import random


db_number=random.randint(1,10)

attempt=0

while(True):

    if attempt==3:

        print("failed")

        break
    
    attempt+=1

    user=int(input("guess a number.."))

    if user==db_number:

        print("yeah..won.!")

        break

    print("try again")