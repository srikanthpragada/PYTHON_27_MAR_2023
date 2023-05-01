class InvalidAmountError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Invalid Transaction Amount : {self.value}"


class Account:
    minbal = 10000

    @staticmethod
    def getminbal():
        return Account.minbal

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        if amount < 1:
            raise InvalidAmountError(amount)

        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Balance")

    def getbalance(self):
        return self.balance


print(Account.getminbal())
a = Account(1, "Andy")
a.deposit(-50000)
a.withdraw(10000)
print(a.getbalance())

