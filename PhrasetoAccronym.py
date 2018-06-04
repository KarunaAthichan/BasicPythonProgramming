#Phrase to Accronym
 
#word=input("Please enter the name: ")
word = "  new technology   "
 
#Strip String spaces
stripped = word.strip()
 
#Change to Uppercase
uppercase = stripped.upper()
print(uppercase)
 
#Split String and put in a List
data = uppercase.split()
print(data)
 
#Iterate List and get a first index in list of string
for i in data:
  print(i[0], end="")
