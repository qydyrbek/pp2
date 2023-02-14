class Bank:
    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance

    def deposit(self , cash):
        self.balance += cash
        print(f'Balance: {self.balance}')

    def withdraw(self , cash):
        if self.balance >= cash:
            self.balance -= cash
            print(f'Balance : {self.balance}')
        else:
            print('Not enough balance')
            print(f'Balance : {self.balance}')

acc=Bank("Yernar",0)
acc.deposit(20000)
acc.withdraw(14605)