# global variable

class Account:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self,n):
        self._balance -= n



def main():
    account = Account() # constructor
    print("Balance:", account.balance)
    account.deposit(200)
    account.withdraw(18)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()