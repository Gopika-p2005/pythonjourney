class Movie:
    
    def __init__(self,name,duration):

        self.name=name

        self.duration=duration

class Booking(Movie):

    def __init__(self, name, duration,no_ticket,ticket_price):

        super().__init__(name, duration)

        self.no_ticket=no_ticket

        self.ticket_price=ticket_price

    def display_booking(self):

        print(self.name,self.duration,self.no_ticket,self.ticket_price)

    def booking_amount(self):

        booking_cash=self.no_ticket*self.ticket_price

        print("total booking amount",booking_cash)

Booking_instance=Booking("leo",180,4,150)

Booking_instance.display_booking()

Booking_instance.booking_amount()