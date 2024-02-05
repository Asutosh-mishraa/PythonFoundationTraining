from bean.Accounts import Account


class SavingsAccount(Account):
    def __init__(self, account_type, account_balance, customer, interest_rate):
        if account_balance < 500:
            raise ValueError("Minimum balance for a savings account must be 500")

        super().__init__(account_type, account_balance, customer)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate
