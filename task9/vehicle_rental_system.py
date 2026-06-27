class Vehicle:

    def __init__(self,brand,model,rental_price_PD):

        self.brand=brand

        self.model=model

        self.rental_per_day=rental_price_PD

class Car(Vehicle):

    def __init__(self, brand, model, rental_price_PD,fuel_type):
        
        super().__init__(brand, model, rental_price_PD)

        self.fuel_type=fuel_type

    def display_car(self):

        print(self.brand,self.model,self.rental_per_day,self.fuel_type)

    def rent(self,day):

        self.day=day

        rent_cash=self.rental_per_day*self.day

        print("rental cost",rent_cash)

car_instance=Car("toyota","innova",2000,"diesel")

car_instance.display_car()

car_instance.rent(10)
