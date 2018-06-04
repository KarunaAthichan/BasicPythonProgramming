r1=int(input("Enter the row1 for matrix1"))
r2=int(input("Enter the row2 for matrix2"))
 
c1=int(input("Enter the column1 for matrix1"))
c2=int(input("Enter the column2 for matrix2"))
 
#column of matrix1 and row of matrix2 should be equal
if c1 == r2:
  print("Valid multiplication")
 
  matrix1=[[0]*c1 for i in range(r1)]
  matrix2=[[0]*c2 for i in range(r2)]
  #result should be row of matrix1 and column of matrix2
  resultant=[[0]*r1 for i in range(c2)]
 
  for i in range(r1):
    for j in range(c1):
      matrix1[i][j]=int(input("Please enter the value for matrix1: "))
 
  print("matrix1: ")
  for m1 in matrix1:
    print(m1)
 
  for i in range(r2):
    for j in range(c2):
      matrix2[i][j]=int(input("Please enter the value for matrix2: "))
     
  print("matrix2: ")
  for m2 in matrix2:
    print(m2)
     
  # iterate through rows of matrix1
  for i in range(len(matrix1)):
   # iterate through columns of matrix2
    for j in range(len(matrix2[0])):
      # iterate through rows of matrix2
       for k in range(len(matrix2)):
           resultant[i][j] += matrix1[i][k] * matrix2[k][j]
 
  print("resultant matrix")
  for r in resultant:
    print(r)
   
else:
  print("Invalid multiplication")
