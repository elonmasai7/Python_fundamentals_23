# It restrict access to certain attributes and
# methods to prevent direct modification
class BankAccount:
    def __init__(self, balance):
        self.__balannce = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balannce += amount

    def get_balance(self):
        return self.__balannce


account = BankAccount(2500)
account.deposit(350)
print("Balance", account.get_balance())
