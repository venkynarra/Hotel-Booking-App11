import pandas as pd
df = pd.read_csv("hotels.csv", dtype = {"id": str})

df_cards = pd.read_csv("cards.csv", dtype = str).to_dict(orient = "records")
df_cards_security = pd.read_csv("card_security.csv", dtype = str)

class Hotel:
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


class Creditcard:
    def __init__(self, number):
        self.number = number  # making attribute of an instance.

    def validate(self, expiration, holder, cvc):
        card_data = {"number":self.number, "expiration":expiration,
                     "holder": holder, "cvc":cvc}
        if card_data in df_cards:
            return  True
        else:
            return False

class SecureCreditcard(Creditcard): #inheriting using Creditcard, this is child class.
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False




print(df)

hotel_ID = input("Enter the id of the Hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():

    credit_card = SecureCreditcard(number = "1234567891234567")
    if credit_card.validate(expiration = "12/26", cvc= "123", holder = "Venky Narra"):

        if credit_card.authenticate(given_password= "mypass"):

            hotel.book()
            name = input("Enter Your Name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication is failed")
    else:
        print("There is a problem with your payment")
else:
    print("Hotel is not Free.")
