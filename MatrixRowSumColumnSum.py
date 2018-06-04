# 3*3 matrix, adding rows and columns

# Get number of rows and columns from user
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))

# Initialise Sum as 0
sum = 0

# Matrix as a list
matrix1 = [[0]*c for i in range(r)]

# As user to enter the values for matrix
for i in range(r):
    for j in range(c):
        matrix1[i][j] = int(input("Please Enter the element for matrix: "))

print("Matrix1 in matrix form: ")
for i in range(r):
    for j in range(c):
        print(matrix1[i][j], end=' ')
    print()

print("*"*25)

print("Matrix 1 as List: ")
for i in matrix1:
    print(i)

print("*"*25)

print("Single matrix row addition: ")
# Keep the column constant for entire rows completion
for i in range(c):
    for j in range(r):
        sum = sum + matrix1[i][j]
    print(sum, end=" ")
    print()
    sum=0


print("*"*25)
# Keep the row constant for entire columns completion
print("Single matrix column addition: ")
for i in range(r):
    for j in range(c):
        sum = sum + matrix1[j][i]
    print(sum, end=" ")
    sum=0