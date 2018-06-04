''' Binary List only applicable for sorted list '''

List = [10,20,30,40,50,60,70,80,90,100]

#set flag location as -1
LOC = -1

element = int(input("Enter the element want to search: "))
#lower limit
L=0
#uppser limit
U=len(List)-1

#Finding the mid position
MID=(L+U)//2

#lower limit less than or equal to upper limit AND mid position element not equal to entered element
while L<=U and List[MID]!= element:
    #entered element less than mid position element
    if element < List[MID]:
        #set upper limit is mid -1
        U=MID - 1
    else:
        L=MID + 1
    #finding the new mid position
    MID=(L+U)//2
    
if List[MID]== element:
    LOC = MID
    print("Location is: ",LOC)

else:
    print("Searching element is not present")
