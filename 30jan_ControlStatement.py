# x=int(input("Enter your number="))
# if x%2==0:
#     print("it is a even number")

# else:
#     print("odd number")



# x=int(input("enter first number="))
# y=int(input("enter first number="))
# if x>y:
#     print("x is greater")

# else:
#     print(f'{y} is greater')    # f string print ka pettern

    
# x=int(input("enter your age="))
# if x>=18:
#     print("you can vote")

# else:
#     print("you can't vote")        



# 3 value compare
# x=int(input("Enter no.1="))
# y=int(input("Enter no.2="))
# z=int(input("Enter no.3="))
# if(x>y and x>z ):
#      print(f'{x} is greate')
# else:
#     if(y>z and y>x):
#         print(f'{y} is greater')
#     else:
#         print("z is greater",z)        



x=int(input("Enter no.1="))
y=int(input("Enter no.2="))
z=int(input("Enter no.3="))
if (x>y and x>z):
    print (f'{x}')
elif (y>z and y>x):
    print(f'{y}')
elif(z>x and z>y):
    print(f'{z}')
elif(x==y and y==z):
    print(f'{x} and {y} and {z} all value are equal')          
elif (x==y):
    print(f'{x} and {y} both are equal')
elif(y==z):
    print(f'{y} and {z} both are equal')
elif(z==x):
    print(f'{z}and {x} both are equal') 

else:
    print("plz enter valid value")             
   

   
    
    
    