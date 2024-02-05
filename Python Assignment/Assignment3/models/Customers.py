class Customer:
    __customer_id_counter = 1

    def __init__(self, first_name=None, last_name=None, email=None, phone_number=None, address=None):
        self.__customer_id = Customer.__customer_id_counter
        Customer.__customer_id_counter += 1
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address

    # Getter methods
    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_address(self):
        return self.__address

    # Setter methods
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_address(self, address):
        self.__address = address

    def print_info(self):
        print("Customer ID:", self.__customer_id)
        print("First Name:", self.__first_name)
        print("Last Name:", self.__last_name)
        print("Email Address:", self.__email)
        print("Phone Number:", self.__phone_number)
        print("Address:", self.__address)


