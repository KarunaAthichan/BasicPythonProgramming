# Method overloading means same method name with different arguments

class Calculator:
    # create a static method
    @staticmethod
    def addNum(x1, x2):
        return x1+x2

    # create a static method
    @staticmethod
    def multiplyNum(x1, x2):
        return x1*x2

    # create a static method
    @staticmethod
    # x3=None means when user doesn't give value for x3, it will be discarded
    def avg(x1,x2,x3=None):
        # if x3 is given, go to the loop
        if x3:
            return (x1+x2+x3)/3.0
        else:
            return (x1+x2)/2.0

# static methos should call as classname.methodname()
print(Calculator.avg(10,20,30))
print(Calculator.avg(10,20))