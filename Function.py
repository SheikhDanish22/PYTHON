''' Function--- block of reusable code.

syntax---
       def fun_name(parameter):
        "doc string"
        {
        
        body of function


        return 
        
        }

      varname=fun_name(argument)  

'''


'''     There are two types of function

1) In-built function--- max(),min(),len(),sum(),eval(),print(),input()
2)User-define function

'''
#Relation below argument and parameters

# positinal argument
'''
def fun_name(x,y):
    return x+y
z=fun_name(4,5)
print(z)

'''


#keyward argument
'''
def add (x,y):
    return x+y
z=add(y=4,x=5)
print(z)
'''
'''
def add(x,y):
    return x+y
p=int(input("Enter number:"))
q=int(input("Enter number:"))
z=add(y=p,x=q)
print(z)
'''


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

# def add (*args):
#     print(args)
#     print(type(args))
#     sum=0
#     for i in args:
#         for x in i:
#          sum=sum+x
#     return sum
# p=eval(input("enter:"))  
# x=add(p)
# print(x)

    
#  nested loop lagane ki jarurat nahi hai.

# def add(*n):
#      sum=0
#      for i in n:
#           sum=sum+i
#      return sum     
    
# x=eval(input("enter:"))
# result=add(*x)
# print(result)    



#key-word Argument
# def show_data(**n):
#     for i,j in n.items(): #keys/values
#         print(f'My {i} is {j}')

# show_data()
# show_data(name='danish',age=26,quli='Msc')    



# def show_data(**n):
#     l=[]
#     for v in n.values():
#         l.append(v)
#     return l
        

# x=eval(input("enter dict:"))
# l1=show_data(**x)    
# print(l1)