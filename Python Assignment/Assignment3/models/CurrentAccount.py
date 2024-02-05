from bean.Accounts import Account


class CurrentAccount(Account):
    def __init__(self, account_type, account_balance, customer, overdraft_limit):
        super().__init__(account_type, account_balance, customer)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit
