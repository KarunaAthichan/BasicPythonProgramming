stack=[]

while True:
    
    print("1.Insert element in stack\n2.Remove element from stack\n3.Display element in stack\n4.exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        if len(stack) == 5:
            print("Sorry, stack is already full")
        else:
            element = int(input("please enter element : "))
            stack.append(element)
            print(element, "inserted successfully")
    elif choice == 2:
        if len(stack) == 0:
            print("Sorry, stack is already empty")
        else:
            element = stack.pop()
            print(element, "was removed successfully")
    elif choice == 3:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
    elif choice == 4:
        print("Thanks You. See you later")
        break
    else:
        print("Invalid Option")

    more = input("Do you want to continue? (y/n): ")
    if more =='Y' or more =='y':
        continue
    else:
        print("Thank you. See you later")
        break
    
