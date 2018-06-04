# defining a function
def sqrt(n):
    # create an unlimited while loop
    while True:
        # multiply the numbers and send result to main function
        yield n * n
        # increment the number
        n = n + 1

# get the start and end number of a square
n = int(input("Enter the start value of a square"))
x = int(input("Enter the end value of a square"))

# use for loop, i gives the squared output (e.g. n=2 means i gives 4)
for i in sqrt(n):

    # if x=10 then, take the next number and stop execution
    if i > ((x + 1) * x):
        break
    # increase the number for below print function actual number display
    n = n + 1
    print("Square of", n - 1, "is", i)