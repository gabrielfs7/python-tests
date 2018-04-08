"""
Example using OO and file manipulation to simple handling Account operations
"""


class Account:
    def __init__(self, file_path):
        self.file_path = file_path

    def deposit(self, amount):
        current_balance = self.balance()

        self.__change_balance(str(current_balance + amount))

    def withdraw(self, amount):
        current_balance = self.balance()

        if current_balance > amount:
            Exception("Amout is bigger than current balance " + str(current_balance))

        self.__change_balance(str(current_balance - amount))

    def balance(self):
        with open(self.file_path, 'r') as file:
            return float(file.read())

    def __change_balance(self, amount):
        with open(self.file_path, 'w+') as file:
            file.truncate()
            file.write(str(amount))
            file.close()


"""
Inheritance example in Python
"""


class Transfer(Account):

    def __init__(self, file_path, fee):
        Account.__init__(self, file_path)

        self.__fee = fee

    def transfer(self, amount):
        self.withdraw(amount)
        self.withdraw(self.__fee)


account = Account("balance.txt")
print(str(account.balance()))
account.deposit(50)
print(str(account.balance()))
account.withdraw(50)
print(str(account.balance()))

transfer = Transfer("balance.txt", 1)
transfer.transfer(24)
print(str(transfer.balance()))
transfer.deposit(25)