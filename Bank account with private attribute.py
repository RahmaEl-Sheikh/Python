class BankAccount:
    __balance=0
    def __init__(self,balance):
        print(self.__balance)
        
    def  get_balance(self):
        print(" get_balance")
        print(self.__balance)
        
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.__balance += amount
        print("\n Amount Deposited:", amount)
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.__balance >= amount:
            self.__balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")  

s = BankAccount(5000)
s.deposit()
s.withdraw()
s.get_balance()