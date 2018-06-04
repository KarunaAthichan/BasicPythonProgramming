for i in range(1,6):
   for j in range(1,i+1):
    print(j, end="")
   print()
print("*" *25)
####################################
for m in range(1,6):
  for n in range(1,7-m):
    print(n, end="")
  print()
print("*" *25)
####################################
for x in range(5):
  print(end=" "*x)
  for y in range(1,6-x):
    print(y,end="")
  print()
print("*" *25)
