# Creating isAddable function
def isAddable(m1,m2):
    if m1 == m2:
        return True
    else:
        return False

# Ceating matricSum function
def matricSum(m1,m2):
    # get the inputs for matrix1 and matrix2
    for i in range(r1):
        for j in range(c1):
            m1[i][j] = int(input("Please Enter the element for first matrix: "))
    for i in range(r2):
        for j in range(c2):
            m2[i][j] = int(input("Please Enter the element for second matrix: "))

    # Print matrix1 and matrix 2
    print("Matrix 1: ")
    for i in m1:
        print(i)
    print("Matrix 2: ")
    for j in m2:
        print(j)

    # perform addition
    for i in range(r1):
        for j in range(c1):
            resultant[i][j] = m1[i][j] + m2[i][j]
    return resultant[i][j]


################ Main Function Starts here #########################################################

# get the number of rows for matrix1
r1 = int(input("Please enter the rows for first matrix: "))
# get the number of columns for matrix1
c1 = int(input("Please enter the columns for first matrix: "))

# get the number of rows for matrix2
r2 = int(input("Please enter the rows for second matrix: "))
# get the number of columns for matrix2
c2 = int(input("Please enter the columns for second matrix: "))

# matrix 1 formation
m1 = [[0]*c1 for i in range(r1)]
# matrix 2 formation
m2 = [[0]*c2 for i in range(r2)]
# resultant matrix formation
resultant = [[0]*c2 for i in range(r2)]

# Call isAddable function and if result is True then call matrix sum function
result = isAddable(m1,m2)
# print(result)

if result == True:
    # calling matricSum function
    matricSum(m1, m2)
    # display the result
    print("Resultant matrix")
    for i in range(r1):
        for j in range(c1):
            print(resultant[i][j], end=' ')
        print()

else:
    print("Matrix addition not possible")