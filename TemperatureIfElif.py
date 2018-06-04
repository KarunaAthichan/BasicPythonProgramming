t = int(input("Enter temperature : "))
if t >= 0 and t < 25:
    print("Cool Day")
elif t >= 25 and t <= 35:
    print("Pleasant Day")
elif t > 35:
    print("Hot Day")
else:
    print("Enter value in positive number")
