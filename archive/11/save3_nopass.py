class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self,account):
        return len(self._transactions)
    
    
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

    
    def __getitem__(self, index):
        return self._transactions[index]
        
    def __iter__(self):
        return iter(self._transactions)
    
    
    def __add__(self, amount:int ):
        if isinstance(amount,int):
            self._transactions.append(amount)
        else:
            raise TypeError

    def __sub__(self, amount:int ):
        if isinstance(amount,int):
            self._transactions.append(-amount)
        else:
            raise TypeError

    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"
        
acc1 = Account('aac1', 100)
acc2 = Account('aac2', 200)

acc1-50
acc1+20
acc1+100
acc1-70

print(acc1 == acc2)

print(acc1)
    
print(list(acc1))

print(acc1[0])

