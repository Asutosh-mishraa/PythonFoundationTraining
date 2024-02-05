from bean.BankRepositoryImpl import BankRepositoryImpl



class BankApp:
    def __init__(self):
        self.bank_service_provider = BankRepositoryImpl()

    def display_menu(self):
        print("Welcome to the Banking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. List Accounts")
        print("8. Get Transactions")
        print("9. Exit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account_menu()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.get_balance()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                self.list_accounts()
            elif choice == "8":
                self.get_transactions()
            elif choice == "9":
                print("Exiting the Banking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account_menu(self):

        self.bank_service_provider.createAccount()

    def deposit(self):
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter the amount: "))
        self.bank_service_provider.deposit(account_number, amount)

    def withdraw(self):
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter the amount: "))
        self.bank_service_provider.withdraw(account_number, amount)

    def get_balance(self):
        account_number = int(input("Enter your account number: "))
        self.bank_service_provider.getAccountBalance(account_number)

    def transfer(self):
        from_account = int(input("Enter the from account number: "))
        to_account = int(input("Enter the from to number: "))
        amount = int(input("Enter the amount: "))
        self.bank_service_provider.transfer(from_account, to_account, amount)

    def get_account_details(self):
        account_number = int(input("Enter the account number: "))
        self.bank_service_provider.getAccountDetails(account_number)

    def list_accounts(self):
        self.bank_service_provider.listAccounts()

    def get_transactions(self):
        account_number = int(input("Enter the account number: "))
        from_date = input("Enter the from date: ")
        to_date = input("Enter the to date: ")
        self.bank_service_provider.getTransactions(account_number,from_date,to_date)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main()
