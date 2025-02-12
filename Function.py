#default argument
'''
def fname(x=0,y=0,z=0):
    print('x=',x)
    print('y=',y)
    print('z=',z)
    return x+y+z
   
    
x=fname(5,5,7)
print('x=',x)
'''

#Singale lenth Argument(*args)

def add (*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        for x in i:
         sum=sum+x
    return sum
p=eval(input("enter:"))  
x=add(p)
print(x)

    


