age = int(input("Enter your age : "))
maxexp = int(input("Enter your maximum experience : "))
if age > 20 and age < 50:
    if maxexp >= 3:
        print("Access Granted")
    else:
        print("You have less experience")
else:
    print("You are age is outside the assigned value")
