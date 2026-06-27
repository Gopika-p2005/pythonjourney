

#  **  -  will accept any number of parameters as dictionary
# **kwargs (key word argumrnts)

def display_student(**kwargs):

    print(kwargs)
    print(kwargs["name"])
    print(kwargs["course"])

display_student(roll=123,name="ajith",course="django")
