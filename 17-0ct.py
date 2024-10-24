t =(23,)  # comma lagana jaruri hai tab tuple batayga 
print(type(t))

t1 =("abcd",)
print(type(t1))


t2 = 1,2,3,4,5   #function
print(type(t2))


#empty tuple
t = ()
t1 = tuple()
print(t,t1)

re =("ajay",101,23,9065749872)
print(re)
re =list(re)
re[3]=9087654321
print(re)
print(type(re))
re = tuple(re)
print(re)
print(type(re))



#multipale assignment
a=100
b=200
print("a=",a,"b=",b)
a,b= 200,100
print("a=",a,"b=",b)