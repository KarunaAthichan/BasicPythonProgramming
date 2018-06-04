import random
n = random.randint(1,10)
print(n)
currentnum = 0
count=0
print("find the correct number")
while n!=currentnum and count<5:
  currentnum=int(input("Please enter the number : "))
  if currentnum>n:
    print("You have entered high number")
  elif currentnum<n:
    print("You have entered low number")
  else:
    print("You have entered exact value :",currentnum)
    break
  count=count+1
if count==5:
  print("You have exceed the attempt")
