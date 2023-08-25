# Banking app. you have different types of bank accounts
# ,such as "savings account" and "checking account".
# Both of these types of accounts share some common properties
# and trait/behaviour but also have specific unique features to
# each type.

class Bankaccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balamce is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}.New balance {self.balance}")
        else:
            print("Insuffient balance")

    def display_balance(self):
        print(f"Account {self.account_number} balance:{self.balance}")


class SavingsAccount(Bankaccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.intrest_rate = 0.03

    def calculat_intrest(self):
        return self.balance * self.intrest_rate

    def display_balance(self):
        super().display_balance()
        print(f"Intrest earned : {self.calculat_intrest()}")


class CheckingAccount(Bankaccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.overdraft_limit = 2000.0

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}.New balance {self.balance}")
        else:
            print("Insufficient amount")


savings_acc = SavingsAccount("EGFTSD", 1500.0)
checiking_acc = CheckingAccount("GF4567", 2000.0)

savings_acc.deposit(690.0)
savings_acc.display_balance()

checiking_acc.withdraw(900.0)
checiking_acc.display_balance()
