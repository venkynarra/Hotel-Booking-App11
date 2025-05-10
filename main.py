import pandas as pd
df = pd.read_csv("hotels.csv")



class Hotel:
    def __init__(self, id):
        pass
    def book(self):
        pass
    def avaliable(self):
        pass


class ReservationTicket:
    def __init__(self,  customer_name, hotel_object):
        pass
    def generate(self):
        pass
print(df)
id = input("Enter the id of the Hotel: ")
hotel = Hotel(id)
if hotel.avaliable():
    hotel.book()
    name = input("Enter Your Name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not Free.")
