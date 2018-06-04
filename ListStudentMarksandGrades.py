# Initialising empty list
List = []

# Get total number of students
num = int(input("Enter the number of students: "))

# Get the marks of students
for i in range(num):
    element = int(input("please enter element : "))
    List.append(element)

print(List)

# Initialise the grades empty
GradeA = 0
GradeB = 0
GradeC = 0
GradeF = 0

# Iterate the entire list
for i in range(len(List)):

    if List[i] >= 80:
        GradeA = GradeA+1
        pass

    elif List[i]>= 60 and List[i]<=79:
        GradeB = GradeB + 1
        pass

    elif List[i]>= 40 and List[i]<=59:
        GradeC = GradeC + 1
        pass

    elif List[i]< 40:
        GradeF = GradeF + 1
        pass

    else:
        print("Incorrect value entered")


print("Total Grade A are :", GradeA)
print("Total Grade B are :", GradeB)
print("Total Grade C are :", GradeC)
print("Total Grade F are :", GradeF)