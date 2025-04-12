sum=0
pro=1
n=int(input("Enter number:"))
while (n>0):
    r=n%10
    sum=sum+r
    pro=pro*r
    n=n//10
if sum==pro:
    print("it is a spy number")
else: 
    print("it is not a spy number")    