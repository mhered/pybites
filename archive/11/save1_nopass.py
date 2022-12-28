class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __lt__(self,account):
        return self.balance <account.balance
    def __le__(self,account):
        return self.balance <=account.balance
    def __gt__(self,account):
        return self.balance >account.balance
    def __ge__(self,account):
        return self.balance >=account.balance
    def __eq__(self,account):
        return self.balance >=account.balance
  
        
acc1 = Account('aac1', 100)
acc2 = Account('aac2', 200)

print(acc1 == acc1)
    
    

