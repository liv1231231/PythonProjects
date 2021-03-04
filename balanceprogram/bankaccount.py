class balance:
    def __init__(self,filepath):
        with open("balance.txt",'r') as file:
            self.balance = int(file.read())


    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open("balance.txt",'w') as file:
            file.write(str(self.balance))

account = balance("balanceprogram//balance.txt")
print(account.balance)
account.deposit(100)
account.commit()
print(account.balance)