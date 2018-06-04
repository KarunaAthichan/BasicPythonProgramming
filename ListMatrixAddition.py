r1 = int(input("Enter the row1 for matrix1"))
r2 = int(input("Enter the row2 for matrix2"))

c1 = int(input("Enter the column1 for matrix1"))
c2 = int(input("Enter the column2 for matrix2"))

# Verify given rows and columns of matrix1 and matrix 2 are equal
if r1 == r2 and c1 == c2:
    # assign rows and columns for matrix1 and matrix2
    matrix1 = [[0] * c1 for i in range(r1)]
    matrix2 = [[0] * c2 for j in range(r2)]
    # resultant equal to matrix1 or matrix2
    resultant = [[0] * c1 for i in range(r1)]

    print(matrix1, "", matrix2)

    # get inputs for matrix1
    for i in range(r1):
        for j in range(c1):
            matrix1[i][j] = int(input("Enter the value for matrix1"))
    print(matrix1)

    # get inputs for matrix2
    for i in range(r2):
        for j in range(c2):
            matrix2[i][j] = int(input("Enter the value for matrix2"))
    print(matrix2)

    # add the matrix 1 and matrix2 and save it in resultant matrix
    for i in range(r1):
        for j in range(c1):
            resultant[i][j] = matrix1[i][j] + matrix2[i][j]

    print("*" * 25)

    # display the result
    for r in resultant:
        print(r)

# when the given rows and columns mismatched, display below message
else:
    print("mismatch rows or columns")