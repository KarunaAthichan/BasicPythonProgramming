n=int(input("enter the number to which want to see prime"))
count=0
if n>1:
    for i in range(2,n+1):
        isprime=True
        for j in range(2,i//2+1):
            if i%j==0:
                isprime=False
                break
        if isprime==True:
            print(i,"is a prime number")
            count=count+1
else:
    print("prime number should be greater than 1")
print("Total prime numbers are ",count)
            
            
                
                
