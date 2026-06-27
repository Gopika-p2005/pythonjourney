"""
inheritance:

child class acquire the properties and methods from parent class

type of inheritance:

single inheritance

multi level inheritance

multiple inheritance


self is a keyword used to represent current class instance

super() is a function used to refer parent class 
"""

class parent:

    def car(self):

        print("glanza")

class child(parent):

    def scooter(self):

        print("activa")

child_instance=child()

child_instance.scooter()

child_instance.car()