List=[10,20,30,40,50,60,70,80,90,100]

element = int(input("Enter the element want to remove: "))

LOC = -1

for i in range(len(List)):
    if element == List[i]:
        LOC = i
        break

if LOC == -1:
    print(element, " is not present in the list")
else:
    print(element, " is in index position ",LOC)
    
