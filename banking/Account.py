from abc import ABCMeta, abstractmethod


class Account(metaclass=ABCMeta):

    @abstractmethod
    def create_account(self, name, initial_deposit):
        pass

    @abstractmethod
    def authenticate(self, name, account_number):
        pass

    @abstractmethod
    def withdraw(self, withdrawal_amount):
        pass

    @abstractmethod
    def deposit(self, deposit_amount):
        pass

    @abstractmethod
    def display_balance(self):
        pass
