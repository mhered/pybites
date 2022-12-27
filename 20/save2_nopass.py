class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager
        
    def __enter__(self):
        self._prev_balance = self.balance
        return self
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.balance<0:
            self.balance = self._prev_balance
            self._prev_balance = None
  
        

