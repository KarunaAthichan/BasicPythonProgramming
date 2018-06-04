#Create empty variables
intList=[]
add=0
avg=0
for i in range(5):
    #Get input number in a loop
    num = int(input("Enter the number "))
    #Append the numbers in a list
    intList.append(num)
print(intList)

#Iterate trough the list
for j in intList:
    #add all the values in the list
    add = add+j

#DIsplay the result
print("Total is ",add)
print("Average is ",add/len(intList))
