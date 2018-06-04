class AccountBank:
    # __accNumber = 0
    # __balance = 0

    def __init__(self, accNumber, balance):
        self.__accNumber = accNumber
        self.__balance = balance

    def getAccNumber(self):
        return self.__accNumber

    def getBalance(self):
        return self.__balance

    def setBalance(self,amount):
        self.__balance = amount

    def credit(self,amount):
        self.__balance += amount

    def debit(self, amount):
        if self.__balance < amount:
            print("amount withdrawn exceeds current balance")
        else:
            self.__balance -= amount

    def __str__(self):
        return "Account class"

myAccount = AccountBank("123456",1000)

print(myAccount)
print(myAccount.getAccNumber())
print(myAccount.getBalance())
myAccount.setBalance(2000)
print(myAccount.getBalance())
myAccount.credit(1000)
print(myAccount.getBalance())
myAccount.debit(500)
print(myAccount.getBalance())
myAccount.debit(4000)