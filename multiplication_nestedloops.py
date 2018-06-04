n=int(input("enter the number "))
while True:
  if n>1 and n<11:
    print("number accept")
    for i in range(1,n+1):
      print()
      for j in range(1,n+1):
        print(i*j,end=" ")
    break
  n=int(input("enter the number again "))
