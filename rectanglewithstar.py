l=int(input("Enter the length "))
w=int(input("Enter the width "))
while True:
    if l>0 and l<101 and w>0 and w<101:
        print("area of rectangle ",l*w)
        print("perimeter of rectangle ",2*(l+w))
        for i in range(1,l+1):
            for j in range(1,w+1):
                print("*",end=" ")
            if i!=l:
                print()
        break
    l=int(input("Enter the length again "))
    w=int(input("Enter the width again "))
    
