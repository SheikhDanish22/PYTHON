x=int(input("Enter number:"))
y=int(input("Enter number:"))
z=int(input("Enter number:"))
min_no=min(x,y,z)

hcf=1
while min_no>0:
    if(x%min_no==0 and y%min_no==0 and z%min_no==0):
     hcf=min_no
     break
    min_no=min_no-1
print(hcf)