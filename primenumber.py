n = int(input("Enter a number : "))
# Set the flag, isprime = "true"
isprime = "true"
''' to find a prime number, start div by 2 to till half of the number;
but n//2+1 is absolute division + 1 number because of for loop'''
if n>1:
    for i in range(2,n//2+1):
        if n%i == 0:
            isprime = "false"
            break
    if isprime == "true":
        print(n, " is a prime number")
    else:
        print(n, " is a composite number")
else:
    print(n, " is not a prime number")
