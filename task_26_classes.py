

class BankAccount:
    def __init__(self,account_num,balance,dop):
        self.account_num = account_num
        self.balance = balance
        self.dop = dop
    def deposit(self,cash):
        self.balance = self.balance + cash
    def withdraw(self,dep):
        if dep > self.balance:
            return "Not Enough Cash in your account"
        elif dep == self.balance:
            inp = input("Would you like to drain your account?(Y/N)")
            while inp != 'Y' and inp != 'N':
                inp = input("Would you like to drain your account?(Y/N)")
            if inp == 'Y':
                self.balance = self.balance - dep
            else:
                return "Thank You.."
        else:
            self.balance = self.balance - dep
            return f"Withdrawal successful. Remaining balance: {self.balance}"
            
    def Checkbalance(self):
        return self.balance
    
    
b1 = BankAccount(1001,1000,'20-10-2025')
print(b1.Checkbalance())
b1.deposit(2000)
print(b1.Checkbalance())
print(b1.withdraw(1000))
print(b1.withdraw(3000))
print(b1.withdraw(2000))