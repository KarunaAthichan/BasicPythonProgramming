#create an empty list
lst=[]
#Create while loop for unlimited loop running
while True:
  print("*"*25)
  print("1.Enter name\n2.Search name\n3.update name\n4.delete name\n5.exit")
  print("*"*25)
 
  n = int(input("Enter the option"))
  if n==1:
    entername = input("Enter the name :")
    print("Entered name is :",entername)
    lst.append(entername)
    print(lst)
 
  elif n==2:
    searchname = input("Search the name :")
    print("Search name is :",searchname)
    position = lst.index(searchname)
    print(searchname," is in ",position," position")
 
  elif n==3:
    modifyname = input("Enter the name you want to modify:")
    updname = input("Enter the name you want to update:")
    curname = lst.index(modifyname)
    lst[curname] = updname
    print(modifyname," is updated with ",updname)
 
  elif n==4:
    deletename = input("Enter the name want to delete:")
    dname = lst.index(deletename)
    print("Deleted name is :",lst.pop(dname))
 
  elif n==5:
    print("Exit from List")
    break
 
  else:
    print("invalid option")
 
  option = input("Enter do you want to continue y/n: ")
  if option =='Y' or option=='y':
    continue
  else:
    break
 
print(lst)
