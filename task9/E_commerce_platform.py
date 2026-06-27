class Product:

    def __init__(self,name,price):

        self.name=name

        self.price=price

class ElectronicProduct(Product):

    def __init__(self, name, price,warrenty_year):

        super().__init__(name, price)

        self.warrenty=warrenty_year

    def display_electronicproduct(self):

        print(self.name,self.price,self.warrenty)

    def discount(self):

        discount_amount=self.price-(self.price*10/100)

        print("price after discount",discount_amount)


ElectronicProduct_instance=ElectronicProduct("laptop",50000,2)

ElectronicProduct_instance.display_electronicproduct()

ElectronicProduct_instance.discount()