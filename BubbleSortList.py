#Bubbles up the largest number at the end and smallest number is at first
''' Total Passes = N-1 (e.g. N is length of List)
Total Comparisions = N-K (e.g. 5 -1, 5-2,... etc...)
K=Current Iteration '''

List = [10,5,7,1,34,78,11,17,99,70,45]

length = len(List)

print("Before Sorted list: ",List)

#Outer loop, 1st to length-1 --> for loop will do it
for k in range(1,length):

    #Iterate from 0th element to length-k
    for j in range(length-k):

        #Compare the current element with next element
        if List[j] > List[j+1]:
            temp = List[j]
            List[j]=List[j+1]
            List[j+1]=temp

print("After Sorted list: ",List)
