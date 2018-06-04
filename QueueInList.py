#import deque function
from collections import deque

#for pop left usage deque([]) below
queue = deque([])

while True:
    print("1.Insert element in queue\n2.Remove element from queue\n3.Display element in queue\n4.exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        if len(queue) == 5:
            print("Sorry, queue is already full")
        else:
            element = int(input("please enter element : "))
            queue.append(element)
            print(element, "inserted successfully")
    elif choice == 2:
        if len(queue) == 0:
            print("Sorry, queue is empty")
        else:
            element = queue.popleft()
            print(element, "was removed successfully")
    elif choice == 3:
        for i in range(len(queue)):
            print(queue[i])
    elif choice == 4:
        print("Thank you. See you later")
        break
    else:
        print("Invalid Option")

    more = input("Do you want to continue? (y/n): ")
    if more =='Y' or more =='y':
        continue
    else:
        print("Thank you. See you later")
        break
    
