'''
List-
    collection of objects
                1) Homogeneoos (same data-type)
                2) Heterogeneoos (diff data type)
    orderd collection

    indexing supported

    Slicing support

    Mutable in nature(different memory address)  

    represented in [] with comma(,) septated objects.


    Ex...




'''

# my_list=[10,10.5,'Neeraj']
# print(my_list)
# print(type(my_list))



#in-built function for list:-

'''
max()----
min()----Homoginus collection hona chahiye
len()----
sum()----
id()
type()

'''
# l2=[10,20,30,40,50,60,70]
# print(max(l2))
# print(min(l2))
# print(sum(l2))
# print(len(l2))
# print(id(l2))
# print(type(l2))





#list method

'''
append()-add one object at last position
sort()-arrenge assending form
extend()-add multipal object in last position
remove()-remove one object from requard position
reverse()-reverse orderd
clear()-only object remove but list dont remove del() collection


'''
#append
# l1=[10,10.5,'neeraj',2,4,8]
# x=[22]
# l1.append(x)
# print("Append",l1)
# y="Neeraj"
# l1.append(y)
# print(l1)
# z=85
# l1.append(z)
# print(l1)

# #extend
# p='Neeraj'
# l1.extend(p)
# print(l1)


# #insert
# l1=[10,10.5,'neeraj',2,4,8]
# print(l1)
# l1.insert(1,'RajaBabu')
# print(l1)


# l1.extend(["a"])
# print(l1)
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)


# append()
'''
my_list=[20,40,"rahul","aman",80]
x=90
my_list.append(x)
print(my_list)

l1=["Aman"]
y="khan","hydrabad"
l1.append(y)
print(l1)
'''


'''
sort()
l1=[10,15,20,5,8,25,22]
l1.sort()
print(l1)
'''

'''extend
l1=[10,20,'rahul']
x='ram',5,10,'aman'
l1.extend(x)
print(l1)
'''

'''remove
l1=[10,20,50,30,40]
l1.remove(50)
print(l1)
'''


'''reverse
l1=[10,20,50,30,40]
l1.reverse()
print(l1)
'''


'''clear()
l1=[10,20,50,30,40]
l1.clear()
print(l1)
'''


'''pop()
l1=[10,20,50,30,40]
l1.pop()
print(l1)
'''

'''insert()
l1=[10,20,40,50]
l1.insert(2,30)
print(l1)


l1=[10,20,40,50]
l1.insert(2,"Rammez")
print(l1)
'''


'''copy()
l1=[1,2,3,4,5]
l2=l1.copy()
print(l2)
'''


'''count()
l1=[10,20,20,30,40]
x=l1.count(20)
print(x)
'''

'''index'''
l1=[10,20,30,40,50,60,70,80]
x=l1.index(40)
print(x)