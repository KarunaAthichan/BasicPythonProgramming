# defining function
def printAsterisks(n):
    # return how many astrisks want to be printed
    return "*"*n


# main program starts here
# get input from user
n = int(input("Enter the numbers of asterisks: "))

# call the function with in print function
print(n,"Asterisks printed", printAsterisks(n))
