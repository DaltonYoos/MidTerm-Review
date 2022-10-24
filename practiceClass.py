'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
class Play:

    def __init__(self,idnumber,name,num_seats,show_date,seat_status):

        self.__idnumber = idnumber
        self.__name = name
        self.__num_seats = num_seats
        self.__show_date = show_date
        self.__seat_status = seat_status
        self.__seat_status = True

    def get_name(self):
        return self.__name

    def get_idnumber(self):
        return self.__idnumber

    def get_num_seats(self):
        return self.__num_seats

    def get_show_date(self):
        return self.__show_date

    def get_seat_status(self):
        return self.__seat_status

    def change_seat_status(self):
        self.__seat_status = False

    def seats_left(self):
        self.__num_seats -= 1


class Booking:

    def __init__(self,client_name,seat_num):
        
        self.__client_name = client_name
        self.__seat_num = seat_num

    def get_client_name(self):
        return self.__client_name
    
    def get_seat_num(self):
        return self.__seat_num


