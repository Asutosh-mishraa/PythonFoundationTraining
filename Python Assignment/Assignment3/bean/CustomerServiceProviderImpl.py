import mysql.connector

from Connection.DBUtil import DBUtil
from Services.ICustomerServiceProvider import ICustomerServiceProvider


class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.db_connection = DBUtil.getDBConn()

    def get_account_balance(self, account_number):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT balance FROM Accounts WHERE account_id = %s", (account_number,))
            result = cursor.fetchone()
            if result:
                return result[0]
            return None
        except mysql.connector.Error as err:
            print("Error:", err)

    def deposit(self, account_number, amount):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE Accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_number))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db_connection.rollback()
            return False

    def withdraw(self, account_number, amount):
        try:
            current_balance = self.get_account_balance(account_number)
            if current_balance is not None:
                cursor = self.db_connection.cursor()
                cursor.execute("SELECT account_type FROM Accounts WHERE account_id = %s", (account_number,))
                account_type = cursor.fetchone()[0]

                if account_type == 'Savings':
                    if current_balance >= amount:
                        new_balance = current_balance - amount
                        cursor.execute("UPDATE Accounts SET balance = %s WHERE account_id = %s",
                                       (new_balance, account_number))
                        self.db_connection.commit()
                        return True
                    else:
                        print("Insufficient balance")
                        return False
                elif account_type == 'Current':
                    cursor.execute("SELECT overdraftLimit FROM Accounts WHERE account_id = %s", (account_number,))
                    overdraft_limit = cursor.fetchone()[0]
                    if (current_balance + overdraft_limit) >= amount:
                        new_balance = current_balance - amount
                        cursor.execute("UPDATE Accounts SET balance = %s WHERE account_id = %s",
                                       (new_balance, account_number))
                        self.db_connection.commit()
                        return True
                    else:
                        print("Withdrawal amount exceeds overdraft limit")
                        return False
            return False
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db_connection.rollback()
            return False

    def transfer(self, from_account_number, to_account_number, amount):
        try:
            if self.withdraw(from_account_number, amount):
                self.deposit(to_account_number, amount)
                return True
            return False
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db_connection.rollback()
            return False

    def get_account_details(self, account_number):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM Accounts WHERE account_id = %s", (account_number,))
            account_details = cursor.fetchone()
            if account_details:
                return account_details
            return None
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_transactions(self, account_number, FromDate, ToDate):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM Transactions WHERE account_id = %s AND transaction_date BETWEEN %s AND %s",
                           (account_number, FromDate, ToDate))
            transactions = cursor.fetchall()
            return transactions
        except mysql.connector.Error as err:
            print("Error:", err)
