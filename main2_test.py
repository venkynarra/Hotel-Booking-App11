import pandas as pd
df = pd.read_csv("hotels.csv", dtype = {"id": str})


class Hotel:  #class methods are coded outside(this is the part of class, not hotel)
    watermakr = "the real estate company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):# book a hotel by changing its availability to no
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)
    def available(self):#check if the hotel is available
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False





class ReservationTicket:
    def __init__(self,  customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
                Thank you for your reservation!
             Here is the booking data:
               Name: {self.customer_name}
                hotel:{self.hotel.name}"""
        return content


