class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balance: float = balance

    def credit(self, amount: float):
        self.balance += amount
        return self.balance

    def debit(self, amount: float):
        if amount > self.balance:
            return "Amount exceeded balance"
        self.balance -= amount
        return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

second_account = Account(5411256, "Peter")
print(second_account.debit(500))
print(second_account.credit(1000))
print(second_account.debit(500))
print(second_account.info())