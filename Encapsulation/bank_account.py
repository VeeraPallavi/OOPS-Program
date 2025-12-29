class BankAccount:
    """Bank Account
    Design a BankAccount class that:
    Has private variables: accountNumber, balance
    Allows deposit and withdraw methods
    Prevents withdrawal if balance is insufficient
    """

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    
acc = BankAccount(123456, 100000)
acc.deposit(2000)
acc.withdraw(3000)
print("Balance:", acc.get_balance())



        
