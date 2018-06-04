string = input("Please enter the name: ")

#convert to lower case to avoid case sensitive
string1 = string.lower()

#Find the length of string
length = len(string1)

flag = True

#set range as length divided by 2
for i in range(length//2):
    #first letter with last letter
    if string1[i] == string1[(length-1) -i]:
        pass
    else:
        flag = False
        break

if flag == True:
    print(string," is a palindrome")

else:
    print(string, " is not a palindrome")



