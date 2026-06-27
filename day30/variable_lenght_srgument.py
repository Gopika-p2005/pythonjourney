

# *args will accept any number of parameter as tuble
#  *  - tuple

#  **  - dictionary
# **kwargs (key word argumrnts)


def add(*argument):

    print(sum(argument))

add(10)
add(10,20)
add(10,20,30)
