class bank:
    def __init__(self):
        self.acc_name=str(input("enter the account name="))
        self.acc_type=input("enter your bank type s/c: ")
        self.acc_no=int(input("enter the acc no:"))
        self.acc_balance=0
    def deposit(self):
        amount=int(input("enter the amount:"))
        self.acc_balance=self.acc_balance+amount
        print("balance=",self.acc_balance)
    def withdraw(self):
         amount=int(input("enter the amount:"))
         if self.acc_balance>=amount:
             self.acc_balance=self.acc_balance-amount
             print("balance=",self.acc_balance)
         else:
             print("insufficient balance")
obj=bank()
while(True):
    opt=int(input("enter your options:1.deposit 2.withdraw 3.exit"))
    if opt==1:
        obj.deposit()
    elif opt==2:
        obj.withdraw()
    elif opt==3:
        break;
    else:
        print("invalid condition")