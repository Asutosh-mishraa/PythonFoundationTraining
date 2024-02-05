import pymysql

from Connection.DBUtil import DBUtil
from Services.IBankRepository import IBankRepository
from bean.Accounts import Account
from models.Customers import Customer
from models.Transactions import Transaction


class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def createAccount(self):
        first_name = input("Enter customer's first name: ")
        last_name = input("Enter customer's last name: ")
        # dob = input("Enter customer's date of birth (YYYY-MM-DD): ")
        email = input("Enter customer's email address: ")
        phone_number = input("Enter customer's phone number: ")
        address = input("Enter customer's address: ")

        customer = Customer(first_name, last_name, email, phone_number, address)


        accType = input("Enter account type (savings/current/zero_balance): ")
        balance = float(input("Enter initial balance: "))

        new_account = Account(accType, balance, customer)

        db_connection = DBUtil.getDBConn()
        cursor = db_connection.cursor()
        try:

            cursor.execute(
                "INSERT INTO Accounts (account_id, customer_id, account_type, balance) VALUES (%s, %s, %s, %s)",
                (new_account.get_account_number(), new_account.get_customer().get_customer_id(),
                 new_account.get_account_type(), new_account.get_account_balance()))

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
        accounts = []
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Accounts"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)

    def calculateInterest(self):
        cursor = self.connection.cursor()
        try:

            cursor.execute("SELECT account_id, balance, interest_rate FROM Accounts")
            accounts = cursor.fetchall()

            for account in accounts:
                account_id, balance, interest_rate = account
                interest_amount = balance * (interest_rate / 100)
                new_balance = balance + interest_amount

                cursor.execute("UPDATE Accounts SET balance = %s WHERE account_id = %s", (new_balance, account_id))
                self.connection.commit()

            print("Interest calculated and updated successfully.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()

    def getAccountBalance(self, account_number):
        with self.connection.cursor() as cursor:
            sql = "SELECT balance FROM Accounts WHERE account_id = %s"
            cursor.execute(sql, (account_number,))
            result = cursor.fetchone()
            if result:
                print(result)
                return(result[0])
            return None

    def deposit(self, account_number, amount):
        current_balance = self.getAccountBalance(account_number)
        if current_balance is not None:
            new_balance = current_balance + amount
            with self.connection.cursor() as cursor:
                sql = "UPDATE Accounts SET balance = %s WHERE account_id = %s"
                cursor.execute(sql, (new_balance, account_number))
            self.connection.commit()
            return new_balance
        else:
            return None

    def withdraw(self, account_number, amount):
        current_balance = self.getAccountBalance(account_number)
        if current_balance is not None:
            new_balance = current_balance - amount
            if new_balance >= 0:
                with self.connection.cursor() as cursor:
                    sql = "UPDATE Accounts SET balance = %s WHERE account_id = %s"
                    cursor.execute(sql, (new_balance, account_number))
                self.connection.commit()
                return new_balance
            else:
                return None
        else:
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        cursor = self.connection.cursor()

        try:

            # Check if both accounts exist
            cursor.execute("SELECT balance FROM Accounts WHERE account_id = %s", (from_account_number,))
            sender_balance = cursor.fetchone()
            cursor.execute("SELECT balance FROM Accounts WHERE account_id = %s", (to_account_number,))
            receiver_balance = cursor.fetchone()

            if sender_balance is None or receiver_balance is None:
                print("Invalid account number.")
                return

            sender_balance = sender_balance[0]
            receiver_balance = receiver_balance[0]

            # Check if sender has sufficient balance
            if sender_balance < amount:
                print("Insufficient funds.")
                return

            # Deduct amount from sender and add to receiver
            sender_balance -= amount
            receiver_balance += amount

            # Update sender's balance
            cursor.execute("UPDATE Accounts SET balance = %s WHERE account_id = %s",
                           (sender_balance, from_account_number))

            # Update receiver's balance
            cursor.execute("UPDATE Accounts SET balance = %s WHERE account_id = %s",
                           (receiver_balance, to_account_number))

            # Record the transaction
            cursor.execute(
                "INSERT INTO Transactions (account_id, transaction_type, amount) VALUES (%s, 'transfer', %s)",
                (from_account_number, -amount))
            cursor.execute(
                "INSERT INTO Transactions (account_id, transaction_type, amount) VALUES (%s, 'transfer', %s)",
                (to_account_number, amount))

            self.connection.commit()
            print("Transfer successful.")

        except Exception as e:
            self.connection.rollback()
            print("Error:", e)

        finally:
            cursor.close()

    def getAccountDetails(self, account_number):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Accounts WHERE account_id = %s"
            cursor.execute(sql, (account_number,))
            result = cursor.fetchone()
            print(result)

    def getTransactions(self, account_number, from_date, to_date):
        transactions = []
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Transactions WHERE account_id = %s AND transaction_date BETWEEN %s AND %s"
            cursor.execute(sql, (account_number, from_date, to_date))
            results = cursor.fetchall()
            for row in results:
                transaction = Transaction(row['transaction_id'], row['account_id'], row['transaction_type'],
                                          row['amount'], row['transaction_date'])
                transactions.append(transaction)
        if results:
            for i in results:
                print(i)
        else:
            print("No transactions found.")

    def __del__(self):
        self.connection.close()
