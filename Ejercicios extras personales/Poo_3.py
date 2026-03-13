class BankAcount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

    def show_balance(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


account1 = BankAcount("Alice", 1000)
account1.show_balance()
account1.deposit(500)
account1.withdraw(200)