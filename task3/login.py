db_username="python"

db_password="python@123"

username =input("enter username:")


password = input("enter password:")


if db_username==username and db_password==password:

    print("login successful")


elif db_username==username or db_password==password:

    print("incorrect passsword")

else:

    print("user not found")