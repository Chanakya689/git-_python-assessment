#Create a BankAccount class where the balance is a private attribute
#  (cannot be accessed directly from outside the class). 
# Provide deposit and withdraw methods to modify the balance safely.
#  Given Input: 
# account = BankAccount(100) 
# account.deposit(50) account.withdraw(200) # 
# This should trigger a warning
#  Expected Output:
#  Deposited 50.
#  New Balance: 150 Insufficient funds! 
# Final Balance: 150

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit(self,r):
         print("Balance Amount:-",self.__balance)
         self.__balance += r
         print("After Deposited Amount",self.__balance)

    def withdraw(self,rupees):
        if rupees > self.__balance:
            print("Funds are not suffcient !!!")  
        else:
            self.__balance -= rupees
            print(f"Withdraw amount is {rupees}")
            print(f"After withdraw balance is {self.__balance}") 

    
    def get_balance(self):
        return self.__balance
         

obj = BankAccount(500)
obj.deposit(600)
obj.withdraw(100)
print(obj.get_balance())

