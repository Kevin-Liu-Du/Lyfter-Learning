class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Withdrawal would go below minimum balance")

        super().withdraw(amount)

acc1 = SavingsAccount(1000, 200)#balance = 1000 min_balance = 200

acc1.withdraw(700) #1000 - 700 < 200, 1000 - 700 = 300, 300 < 200 = FALSE does not enter the error 
#super().withdraw(amount) 
print(acc1.balance) #300

acc1.withdraw(200)
