def pw(x, n):
    res = x ** n
    return res


x = int(input("Enter the value to be powered: "))
n = int(input("Enter the power: "))

print("Result for", x, "to the power", n, "is", pw(x, n))