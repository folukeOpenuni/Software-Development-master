#create a class called Ticket with private attribute number and price
class Ticket:
    def __init__(self, number, price):
        self.__ticket_number = number
        self.__ticket_price = price
  
    def get_price(self):
        return self.__ticket_price
    
    def get_number(self):
        return self.__ticket_number

    def toStr(self):
        return "Ticket number: " + str(self.__ticket_number) + ", Price: " + str(self.__ticket_price)