''' Advance Python
     higher order function--
           1. map()
           2.filter()
           3.reduce()
           4.lambda
           5.decoretor
           6.generator


 map()-----------syntex
            collection(iterator)
            def fname():
                   ........
                   .........
                   return
            map(fname,collection)       


'''
#Map()
# my_list=[10,20,30,40,50]
# def dic(x):
#     return x**2
# x=map(dic,my_list)
# print(tuple(x))


'''
   filter()
'''
# my_tuple=(70,75,60,59,40,60,80)
# def grater_60(x):
#     if x>60:
#      return x
# x=tuple(filter(grater_60,my_tuple))
# print(x)



#reducec()
# from functools import reduce
# my_tuple=(10,20,30,60,40,50)
# def max_digit(x,y):
#     if( x>y):
#         return x
#     else:
#         return y
# x=reduce(max_digit,my_tuple)
# print(x) 



#lamda()-- it is a keyword and function
#x= lambda variables:expression
            #n no. of
            #variables

# x= lambda x,y,z,p,q,r:x+y-z/p%q//r
# print(x(1,2,3,4,5,6))

# y=lambda x:x**2
# print("5 ka square=",y(5))

# z=lambda x:x+10
# print(z(15))

from functools import reduce
# my_list=[10,15,20,25,30,35,40,45,50]
# x=list(filter(lambda x:x%2==0,my_list))
# print("Evan Number=",x)
# z= list(map(lambda x:x**2,x))
# print("Evan number square=",z)
# y=reduce(lambda x,y:x+y,z)
# print("Total of Evan number square=",y)




# number=[10,15,20,25,30,35]
# even_num=list(filter(lambda x:x%2==0,number))
# print("Evan number=",even_num)
# sum=reduce(lambda x,y:x+y,even_num)
# print("Sum=",sum)
# square=sum**2
# print("square=",square)


# Decoretor

# def outer_function(func):
#     def inner_function(x,y):
#         x=x+5
#         y=y+5
#         data=func(x,y)
#         return data
#     return inner_function  
# @ outer_function
# def main_function(x,y):
#     z=x+y
#     return z
# data=main_function(5,10)
# print(data)    



#Generator --- yield keyword use

def even(n):
    i=2
    while i<=n:
        yield
        i=i+2
n=int(input("Enter your number="))        
data=even(n)
print(data)  
data1=even(n)
print(data1)      
