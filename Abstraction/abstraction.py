from abc import ABC, abstractmethod
class FundTranfer(ABC):
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    
    def validate(self, amount):
        if len(str(self.account_number)) == 10 and amount < self.balance and amount > 0:
            return True
        return False
    
    @abstractmethod
    def transfer(self,amount):
        pass

class NEFTTransfer(FundTranfer):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    
    def transfer(self, amount):
        sc = amount * 0.05
        if(amount + sc < self.balance):
            self.balance = self.balance - (amount + sc)
            return True
        return False
    
class IMPSTransfer(FundTranfer):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    
    def transfer(self, amount):
        sc = amount * 0.02
        if(amount + sc < self.balance):
            self.balance = self.balance - (amount + sc)
            return True
        return False
    
class RTGSTransfer(FundTranfer):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    
    def transfer(self, amount):
        if(amount  < self.balance and amount >= 10000):
            self.balance = self.balance - (amount)
        return False

def main():
    an = int(input("Entr your account number: "))
    bal = int(input("Enter your account balance: "))
    print("Enter your choice")
    print("1. NEFT\n2. IMPS\n3. RTGS\n")
    choice = int(input())
    if choice == 1:
        ref = NEFTTransfer(an,bal)
    elif choice == 2:
        ref = IMPSTransfer(an, bal)
    elif choice == 3:
        ref == RTGSTransfer(an, bal)
    
    if ref.validate():
        if ref.transfer():
            print("Transfer occurred successfully")
            print(f"Remaining balance is {ref.balance}")
        else:
            print("Transfer could not be made")
    else:
        print("Account number or transfer amout seems to be wrong")

main()
