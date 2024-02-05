from abc import ABC, abstractmethod
from datetime import datetime


class IBankRepository(ABC):
    @abstractmethod
    def createAccount(self):
        pass

    @abstractmethod
    def listAccounts(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass

    @abstractmethod
    def getAccountBalance(self, account_number: int):
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float):
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float):
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        pass

    @abstractmethod
    def getAccountDetails(self, account_number: int):
        pass

    @abstractmethod
    def getTransactions(self, account_number: int, FromDate: datetime, ToDate: datetime):
        pass
