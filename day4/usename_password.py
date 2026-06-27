db_user_name = "django@123" 

db_password = "password@123" 


username = input("enter username")

password = input("enter password")

if username==db_user_name and password==db_password:

    print("access granted")

else:
    
    print("access denied") 