number = int(input("Enter the value : "))
#set f=1
f=1
#starts from given number and ends in 1 with -1 lesser each time
for num in range(number,0,-1):
   f=f*num
print("The factorial of ",number," is : ",f)
