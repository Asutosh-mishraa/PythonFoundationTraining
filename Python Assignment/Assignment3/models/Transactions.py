class Transaction:
    def __init__(self, account, description, transaction_type, transaction_amount, date_time):
        self.account = account
        self.description = description
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.date_time = date_time

    def get_transaction_details(self):
        print("Account:", self.account.get_account_number())
        print("Description:", self.description)
        print("Transaction Type:", self.transaction_type)
        print("Transaction Amount:", self.transaction_amount)
        print("Date and Time:", self.date_time)
