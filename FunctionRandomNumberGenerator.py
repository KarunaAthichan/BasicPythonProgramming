# import random function
import random


# define a function
def create_list(n):
    # create an empty list
    list = []

    # iterate for loop till the user entered number
    for i in range(n):
        # generate random number from 1 to 6
        rnum = random.randint(1, 6)
        # append the generated random number in a list
        list.append(rnum)
    # return the list
    return list


# get the total number of random number should be generated from user
n = int(input("Enter the total random number to be generated"))

# calling the function create_list
my_list = create_list(n)
# print the result
print(my_list)