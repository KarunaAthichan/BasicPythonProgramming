# define a function
def front_times(string, front, n):
    # create an empty string
    str = ""

    # get value of n and iterate it, number of times the string should repeat
    for k in range(n):

        # get value of front and iterate till the character in a string
        for i in range(front):
            # append the string
            str = str + string[i]
    # return the value
    return str


# Get the input string from user
string = input("Enter the String want to display")

# Get the number of characters in string to display
front = int(input("Enter the number of characters want to display"))

# Get number of times the string should repeat
n = int(input("Enter number of times string should display"))

# Call the function and get the return value as output
print("Output is", front_times(string, front, n))