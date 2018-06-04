class Account:

    # initiate at class level
    __accNumber = 0
    __balance = 0

    def __init__(self, accNumber, balance = 1000):
        self.setAccNumber(accNumber)
        self.setBalance(balance)


    def getAccountNumber(self):
        return self.__accNumber


    def setAccNumber(self, accNumber):
        try:
            if len(accNumber) != 10 or not accNumber.isdigit():
                raise Exception("Invalid Account Number!")
            else:
                self.__accNumber = accNumber
        except Exception as e:
            print(e.args)


    def getBalance(self):
        return self.__balance


    def setBalance(self, amount):
        try:
            if amount >= 0:
                self.__balance = amount
            else:
                raise Exception("Amount should be greater than zero or "
                                "equal to zero")
        except Exception as e:
            print(e.args)


    def credit(self, amount):
        try:
            if amount > 0:
                self.__balance += amount
            else:
                raise Exception("Amount should be positive")
        except Exception as e:
            print(e.args)


    def debit(self, amount):
        try:
            if self.__balance < amount:
                raise Exception("amount withdrawn exceeds the current balance")
            else:
                self.__balance -= amount
        except Exception as e:
            print(e.args)


    def __str__(self):
        return "Account Number: {}, Balance: {}".format(self.getAccountNumber(),
                                                        self.getBalance())
myAccount = Account("123456")
print(myAccount)
print(myAccount.getAccountNumber())
print(myAccount.getBalance())
myAccount.setBalance(2000)
print(myAccount.getBalance())
myAccount.credit(1000)
print(myAccount.getBalance())
myAccount.debit(500)
print(myAccount.getBalance())
myAccount.debit(4000)
myAccount.setBalance(-100)
myAccount.setAccNumber(62546248623)
myAccount.credit("1245")