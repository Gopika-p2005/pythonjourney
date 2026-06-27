db_user="admin"
db_password="1234"

attempt=0

while(attempt<3):

    user=input("username")

    password=input('passsword')

    if db_user==user and db_password==password:

        print("login successful")

        break

    else:
        print("wrong")

        attempt+=1

    if attempt==3:
        print("account locked")