class Parent:

    def bike(self):

        print("passion pro")


    def car(self):

        print("swift")

class Child(Parent):

    def bike(self):
        
        print("gurilla")

    def car(self):

        print("thar")

child_instance=Child()

child_instance.bike()

child_instance.car()
