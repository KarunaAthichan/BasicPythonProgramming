a=[10,23,47,48,63,93,105,5]
print (max(a))
print (min(a))

#Set variable for max as 0
max = 0

#Get the total index of list a
for i in range(len(a)):
    #Identify the maximum
    if a[i]>max:
        max=a[i]
print("Maximun number is ",max)

#Set minimum value as first value in list a
min=a[0]

#Get the total index of list a
for j in range(len(a)):
    #Identify the minimum
    if a[j]<min:
        min=a[j]
print("Minimum number is ",min)
