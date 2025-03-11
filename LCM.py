x=eval(input("Enter number:"))
y=eval(input("Enter number:"))
max_no=max(x,y)

while True:
    if (max_no%x==0 and max_no%y==0):
        break
    max_no=max_no+1
print(max_no)    