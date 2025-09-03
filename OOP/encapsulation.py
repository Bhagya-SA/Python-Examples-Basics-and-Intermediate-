# encapsulation.py
# Example of Encapsulation in Python

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable (name mangling)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

# Using the class
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)

print("Account Balance:", account.get_balance())

# Direct access not possible
# print(account.__balance)  # ❌ Error
