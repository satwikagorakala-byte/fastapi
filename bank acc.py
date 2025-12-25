class BankAccount:
    def __init__(self,AccountName,InitialDeposit,Balance=0):
        self.AccountName=AccountName
        self.InitialDeposit=InitialDeposit
        self.Balance=InitialDeposit
    
    def deposite(self,DepositAmount):
        self.DepositAmount=DepositAmount
        if(self.DepositAmount>=100):
            ccccself.Balance=self.Balance+self.DepositAmount
            return self.Balance
        else:
            return "not allowed"
        
    def withdraw(self,amount):
        self.amount=amount
        if(amount>=100):
            self.Balance=self.Balance-self.amount
            return self.Balance
        


p=BankAccount("Satwika",1000)
p.deposite(1000)
p.withdraw(500)

p.deposite(1500)
p.withdraw(300)

p.deposite(900)
p.withdraw(300)





class BankAccount:
    def __init__(self,AccountName,InitialDeposit):
        self.Balance = 0
        self.AccountName=AccountName
        #self.InitialDeposit=InitialDeposit
        self.Balance=InitialDeposit
    
    def deposite(self,DepositAmount):
        #self.DepositAmount=DepositAmount
        if(DepositAmount>=100):
            self.Balance=self.Balance+DepositAmount
            print(f'Balance for account of {self.AccountName} after deposit of {DepositAmount} is {self.Balance}')
            return self.Balance
        else:
            print("Deposit below 100 Rupees is not allowed")
            print(f'Balance for account of {self.AccountName} after deposit of {DepositAmount} is {self.Balance}')
            return self.Balance
        
    def withdraw(self,withdrawamount):
        #self.amount=amount
        if(withdrawamount>=100):
            self.Balance=self.Balance-withdrawamount
            print(f'Balance in account of {self.AccountName} after withdrawal of {withdrawamount} is {self.Balance}')
            return self.Balance
        

p=BankAccount("Satwika",1000)
p.deposite(1000)
p.withdraw(500)

p.deposite(1500)
p.withdraw(300)

p.deposite(900)
p.withdraw(300)



