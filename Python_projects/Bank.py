class Bank:
    def __init__(self, name, account_type, balance):
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return "Name: {0}\nAccount Type: {1}\nBalance: {2}".format(self.name, self.account_type, self.balance)

# Create a Bank object
b = Bank("John", "Saving", 1000)

# Perform operations and print the results
b.withdraw(100)
print(b)

b.deposit(100)
print(b)

b.set_balance(1000)
print(b)

print(b.get_balance())
