

class Account:
    def __init__(self, file_path):
        self.file_path = file_path

    def deposit(self, amount):
        current_balance = self.balance()

        new_balance = current_balance + amount

        with open(self.file_path, 'w+') as file:
            file.truncate()
            file.write(str(new_balance))
            file.close()

    def withdraw(self, amount):
        current_balance = self.balance()

        if current_balance > amount:
            Exception("Amout is bigger than current balance " + str(current_balance))

        new_balance = current_balance - amount

        with open(self.file_path, 'w+') as file:
            file.truncate()
            file.write(str(new_balance))

    def balance(self):
        with open(self.file_path, 'r') as file:
            return float(file.read())


account = Account("balance.txt")

print(str(account.balance()))

account.deposit(50)

print(str(account.balance()))

account.withdraw(50)

print(str(account.balance()))