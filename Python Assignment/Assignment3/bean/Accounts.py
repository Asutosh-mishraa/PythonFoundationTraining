
class Account:
    __last_account_number = 1000

    def __init__(self, account_type, account_balance, customer):
        Account.__last_account_number += 1
        self.__account_number = Account.__last_account_number

        self.__account_type = account_type
        self.__account_balance = account_balance
        self.__customer = customer

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_account_balance(self):
        return self.__account_balance

    def get_customer(self):
        return self.__customer

    # Setter methods
    def set_account_balance(self, new_balance):
        self.__account_balance = new_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print("Withdrawal successful. Remaining balance:", self.__account_balance)
        else:
            print("Insufficient funds")

    def calculate_interest(self):
        # Assuming fixed interest rate of 4.5%
        interest = self.__account_balance * 0.045
        self.deposit(interest)

    def print_info(self):
        print("Account Number:", self.__account_number)
        print("Account Type:", self.__account_type)
        print("Account Balance:", self.__account_balance)
        print("Customer:", self.__customer.get_first_name(), self.__customer.get_last_name())


