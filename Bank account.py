class BankAccount:
    account_number=""
    balance=0
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        print("start")
        print("your id is: %s" %self.account_number)
        print("your balance in is: %.2f " %self.balance)
    def __del__(self):
        print("destructor: warning!!!")

r1=BankAccount("1000000",70000000)
del r1
