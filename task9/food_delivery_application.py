class Restaurent:

    def __init__(self,name,location):

        self.name=name

        self.location=location

class Order(Restaurent):

    def __init__(self, name, location,amount):

        super().__init__(name, location)

        self.amount=amount

    def display_order(self):

        print(self.name,self.location,self.amount)

    def delivery(self):

        if self.amount>=500:

            charge=0

        else:

            charge=50

        print("delivery charge",charge)

order_instance=Order("food hub","kochi",400)

order_instance.display_order()

order_instance.delivery()
