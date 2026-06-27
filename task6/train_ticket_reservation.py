available_seats = 50

seats = int(input("Enter seats required: "))

if seats <= available_seats:
    available_seats -= seats
    print("Booking Successful")
    print("Remaining Seats:", available_seats)
else:
    print("Seats Not Available")