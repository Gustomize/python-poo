from abc import ABC

from Account import *
from random import randint


class SavingsAccount(Account, ABC):
    def __init__(self):
        self.savings_accounts = {}
        self.account_number = 0

    def create_account(self, name, initial_deposit):
        print()

        self.account_number = randint(10000, 99999)
        self.savings_accounts[self.account_number] = [name, initial_deposit]

        print("Account creation has been successful. Your account number is ",
              self.account_number)

        print()

    def authenticate(self, name, account_number):
        print()

        if account_number in self.savings_accounts.keys():

            if self.savings_accounts[account_number][0] == name:
                print("Authentication Successful")
                self.account_number = account_number

                print()

                return True

            else:
                print("Authentication Failed")
                print()

                return False
        else:
            print("Authentication Failed")
            print()

            return False

    def withdraw(self, withdrawal_amount):
        print()

        if withdrawal_amount > self.savings_accounts[self.account_number][1]:
            print("Insufficient balance")
        else:
            self.savings_accounts[self.account_number][1] -= withdrawal_amount
            print("Withdrawal was successful.")
            self.displayBalance()

        print()

    def deposit(self, deposit_amount):
        print()

        self.savings_accounts[self.account_number][1] += deposit_amount

        print("Deposit was successful.")

        self.account_number()

        print()

    def display_balance(self):
        print("Avaialble balance: ",
              self.savings_accounts[self.account_number][1])
