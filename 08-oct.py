# # list = [23,45,6,7,88]
# # # print(list)

# # #append------>  list.append(element)
# # list.append(10)
# # print(list)
# # list.append(["mango","banana"])
# # print(list)
# # print(list[6][1])

# # list.append(["200/kg","50/dozen"])
# # print(list)
# # list.append(7)(["apple","200/kg"])
# # print(list)


# # list =[]
# # print(list)
# # list.append(["mango","banana"])
# # print("\n")
# # list.append(["200/kg","50/dozen"])
# # print(list)
# # list[0].append(["apple"])
# # print("\n")
# # print(list)
# # print("\n")
# # list[1].append(["240/kg"])
# # print("\n")
# # print(list)


# #Extened

# # lis =['mango','banana','apple']
# # print(lis)
# # # lis.extend(45)error
# # print(lis)
# # lis.extend(["Papaya","Pinapple"])
# # print(lis)
# # print(lis[1])
# # print(lis[-2])


# #insert

# # lis =['mango','banana','apple']
# # print(lis)
# # lis.insert(1,"kaju")
# # lis.insert(0,"Kishmish")

# # print(lis)
# # lis[2]="akhroth"
# # print(lis)

# #len(),max(),min(),sum();
# lis =['mango','banana','apple']
# print(lis)
# lis1=[23,33,44,-5,77]
# print(lis1)
# m= max(lis1)
# n= min(lis1)
# print(m)
# m = max(lis)
# m = min(lis)
# print(m)

# l= len(lis1)
# print(l)
# a=len(lis1)
# print(a)
# a=max(lis1)
# print("max=",a)
# a=min(lis1)
# print("min=",a)

# a=sum(lis1)
# print("sum=",a)


# '''
#     dot operator (method) operator (methoods)
#     function without using any dot operator



#     index function--------(important)
         


# '''

# nums =[2,3,45,43,5,6,45,99,66,45,56]
# # index----- index(element,start,end)
# a=nums.index(45,0)
# print(a)
# b=nums.index(45,a+1)
# print(b)
# c=nums.index(45,b+1)
# print(c)
# print("45=",a,b,c)

# # index() reurn index value of element passed,
# # we can give maximum of 3 parameter in index()
# # in first parameter , u have to pass the element
# # itself,
# # and second --->start
# # thired --->end(excluded)
# # if element is not found it throws an exception.


# #count function----- its is return frecquency

# # a=nums.count(45)
# # print("count=",a)

# # #sort (asending order)---None return
# # #                     inplace function
# # #                     no need of extra list(object)
# # nums.sort()
# # print(nums)
# # nums.sort(reverse=True)
# # print(nums)


# # reverse

# # list =['ajay','gagan','magan']
# # print(list)
# # # list.reverse()# inplace
# # print(list)

# # delete function
# # pop()
# # remove()
# # clear()
# # del statement()----return deleted element

# # list =['ajay','gagan','magan']
# # deleted_value=list.pop()
# # print(list)
# # print(deleted_value)


# #  non return       return
# #  append()          count()
# #  extend()           index()
# #   sort()             len()
# #   reverse()          max()
# #   insert()           min()
# #     (non )           sum()
# #                      pop()


# # list =['ajay','gagan','magan']
# # delete=list.pop(1)
# # print(list)
# # print(delete,list)

# #remove
# # list =['ajay','gagan','magan','chagan','sagan','chagan']
# # print(list)
# # d=list.remove('chagan')
# # print(list)
# # d=list.remove('chagan')
# # print(list)


# #clear
# # list =['ajay','gagan','magan','chagan','sagan','chagan']
# # print(list)
# # d=list.clear()
# # print(list)

 #del
# list =['ajay','gagan','magan','chagan','sagan','chagan']
# print(list)
# del list
# print(list)






#slice
list =['ajay','gagan','magan','chagan',56,'sagan','chagan','vivek']
a=list[2 : 7 : 2 ]
print(a)


#   0 1  2     3     4  5  6   7     8  9 10
lis1=[12,3,44, 'danish',56,7,88,'ankur',33,4,5]
#    -11 -10 -9   -8    -7 -6 -5   -4    -3 -2 -1
a=lis1[7:2:-1]
print(a)
# a=lis1[-4:-9:-1]
# print(a)
# a= lis1[::-1]
# print(a)
# #===============================================================================
lis2="we are here to learn python.and sliching is very helpful"
a=lis2[7:20]
print(a)
a=lis2[32:]
print(a)
a=lis2[::-1]
print(a)
print(lis2[3:19:3])
print(lis2[:21] +"cpp"+lis2)




