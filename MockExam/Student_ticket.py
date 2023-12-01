#create a student class which inherits from ticket
class StudentTicket(Ticket):
    def __init__(self, number, price,  student_name):
        super().__init__(number, price)
        self.__student_name = student_name

        
#