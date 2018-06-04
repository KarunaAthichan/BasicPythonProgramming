#[0]*3 --> columns, range(4)--> rows
List=[[0]*3 for i in range(4)]
print(List)

#length of the list, e.g. 4 rows those are separated by commas
for row in range(len(List)):
    #get the column detail of first list
    for column in range(len(List[0])):
        #get the input
        List[row][column]=int(input("Please enter thee value :"))

#get the row from list
for row1 in List:
    #get the column from list
    for column1 in row1:
        print(column1, end=" ")
    print()
        
    
