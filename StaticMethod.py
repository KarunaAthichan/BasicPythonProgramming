class Calculator:

    # static method should start with @staticmethod
    @staticmethod
    def add(x1, x2):
        return x1+x2

    @staticmethod
    def multiply(x1, x2):
        return x1*x2

print(Calculator.add(10, 20))
print(Calculator.multiply(20, 30))