#simple bank account class
class BankAccount:# BankAccount class
    def __init__(self,initial_balance=0):
        self .__account_balance = initial_balance # private variable to store the balance
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    def display_balance(self):
        print(f"current balance : ${self.__account_balance}")
