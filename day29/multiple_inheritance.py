class Mother:

    def dance(self):

        print("mother dancing skill...")

class Father:


    def coding(self):

        print("father coding skill...")

class Child(Mother,Father):

    def sleeping(self):

        print("child sleeping skill...")

child_instance=Child()

child_instance.sleeping()
child_instance.coding()
child_instance.dance()
