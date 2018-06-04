# Enter the list of subjects in a List
Subjects = ["Math", "Physics", "Chemistry", "Biology"]

# Enter the list of students in a List
Students = ["Maaz", "farooq", "maria", "aslam"]

# Enter the variables going to use
stud = 0
subj = 0
IndivMarks = 0
StudTotMarks = 0
Avgmarks = 0

# Create an empty mark List
marks=[]

# Enter the marks of each subject for every student
marksofMaaz = [55,45,67,67]
marksoffarooq = [54,76,98,65]
marksofmaria = [87,65,54,98]
marksofaslam = [76,98,65,43]

# Add the marks of each student to the List
marks.append(marksofMaaz)
marks.append(marksoffarooq)
marks.append(marksofmaria)
marks.append(marksofaslam)

# marks become a 2 dimension List
print(marks)

print("Press 1 to find all the marks of a student\nPress 2 to find the marks of single subject of a student\nPress 3 to find the total marks of a student\nPress 4 to find the average of marks of a student")

print(Students)
print(Subjects)

# Get a choice from user
choice = int(input("Please enter your choice: "))

if choice == 1:
    while True:
        # Get the student name
        stud = input("Name of a student: ")
        # If student is present go out of While loop, else ask user to enter valid student name
        if stud in Students:
            print(stud, " is present in students list")
            break
        else:
            print("Please enter the correct name")
            continue

    # Find the total subject and iterate it
    for i in range(len(Subjects)):
        # Iterate the subjects of a single student
        IndivMarks = marks[Students.index(stud)][i]
        print(Subjects[i],"mark is", IndivMarks)

###################################################################################################################

elif choice == 2:
    while True:
        # Get the student name
        stud = input("Name of a student: ")
        # If student is present go out of While loop, else ask user to enter valid student name
        if stud in Students:
            print(stud, " is present in students list")
            break
        else:
            print("Please enter the correct name")
            continue

    while True:
        # Get the subject
        subj = input("Name of the subject: ")
        # If subject is present go out of While loop, else ask user to enter valid subject
        if subj in Subjects:
            print(subj, " is present in subjects list")
            break
        else:
            print("Please enter the correct subject")
            continue

    print(stud,"mark for",subj,"is",marks[Students.index(stud)][Subjects.index(subj)])

###################################################################################################################

elif choice == 3:
    while True:
        # Get the student name
        stud = input("Name of a student: ")
        # If student is present go out of While loop, else ask user to enter valid student name
        if stud in Students:
            print(stud, " is present in students list")
            break
        else:
            print("Please enter the correct name")
            continue

    # Find the total subject and iterate it
    for i in range(len(Subjects)):
        # Add the total marks of a student
        StudTotMarks = StudTotMarks + marks[Students.index(stud)][i]
    print("Total mark",stud," is", StudTotMarks)

###################################################################################################################

elif choice == 4:
    while True:
        # Get the student name
        stud = input("Name of a student: ")
        # If student is present go out of While loop, else ask user to enter valid student name
        if stud in Students:
            print(stud, " is present in students list")
            break
        else:
            print("Please enter the correct name")
            continue

    # Find the total subject and iterate it
    for i in range(len(Subjects)):
        # Add the total marks of a student
        StudTotMarks = StudTotMarks + marks[Students.index(stud)][i]

    # Finding the average of student
    Avgmarks = StudTotMarks / len(Subjects)
    print("Average for",stud," is", Avgmarks)

###################################################################################################################

else:
    print("Enter a valid choice")
