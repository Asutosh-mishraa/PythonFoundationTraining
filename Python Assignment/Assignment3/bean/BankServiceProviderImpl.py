import pymysql

from Connection.DBUtil import DBUtil
from Services.IBankServiceProvider import IBankServiceProvider
from bean.Accounts import Account
from bean.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from models.Customers import Customer
from models.SavingsAccount import SavingsAccount


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branchName, branchAddress):
        super().__init__()
        self.branchName = branchName
        self.branchAddress = branchAddress
        self.accountList = []
        self.transactionList = []

    def create_account(self):
        first_name = input("Enter customer's first name: ")
        last_name = input("Enter customer's last name: ")
        email = input("Enter customer's email address: ")
        phone_number = input("Enter customer's phone number: ")
        address = input("Enter customer's address: ")

        customer = Customer(first_name, last_name, email, phone_number, address)


        accType = input("Enter account type (savings/current/zero_balance): ")
        balance = float(input("Enter initial balance: "))

        new_account = Account(accType, balance, customer)

        self.accountList.append(new_account)
        db_connection = DBUtil.getDBConn()
        cursor = db_connection.cursor()
        try:

            cursor.execute(
                "INSERT INTO Accounts (account_id, customer_id, account_type, balance) VALUES (%s, %s, %s, %s)",
                (new_account.get_account_number(), new_account.get_customer().get_customer_id(), new_account.get_account_type(), new_account.get_account_balance()))

            db_connection.commit()

            print("New account added to the database.")

        except pymysql.Error as e:
            print(f"Error occurred: {e}")
            db_connection.rollback()

        finally:
            cursor.close()
            db_connection.close()
        return new_account.get_account_number()

    def listAccounts(self):
        print("List of Accounts:")
        for account in self.accountList:
            print(f"Account Number: {account.get_account_number()}, Account Type: {account.get_account_type()}, Balance: {account.get_account_balance()}")

    def getAccountDetails(self, account_number):
        for account in self.accountList:
            if account.accNo == account_number:
                print("Account Details:")
                print(f"Account Number: {account.get_account_number()}")
                print(f"Account Type: {account.get_account_type()}")
                print(f"Balance: {account.get_account_balance()}")
                customer = account.get_customer()
                print(f"Customer ID: {customer.get_customer_id()}")
                print(f"Customer Name: {customer.get_first_name()} {customer.get_last_name()}")
                print(f"Customer Email: {customer.get_email()}")
                print(f"Customer Phone Number: {customer.get_phone_number()}")
                print(f"Customer Address: {customer.get_address()}")
                return
        print("Account not found.")

    def calculateInterest(self):
        print("Calculating interest for savings accounts:")
        for account in self.accountList:
            if isinstance(account, SavingsAccount):
                interest = account.calculate_interest()
                new_balance = account.get_account_balance() + interest
                account.set_account_balance(new_balance)
                print(f"Interest of {interest} added to account {account.get_account_number()}")
        print("Interest calculation completed.")
