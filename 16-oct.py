nu =  (12,45) + (23,67)
nu = nu + (89,90)
print(nu)
#     00    01      10  11
l=[["ajay","aman"],(45,67)]# tupele ke ander change nahi hoga.
#print(type(l[1]))
#l=[1][0]=90   # we cant change
l[0][0]="vijay"# we can change
print(l)


l=(34,55,3,4,[56,555])
l[4][1]=9999 # we can change
print(l)


lis=[["vikas","vinay"],(45,[67,44])]
lis[1][1][0]=99999
lis[0][0]=20
#lis[1][1]=54   we cant change 
print(lis)


#len(), max(),min(),sum(),index(),count().

t=(23,4,5,78,9)
a=t.count(4)
print(a)


# t=(23,4,5,78,9)
# t.len()
# print(t)


#sorted() ----> return sorted list
t = (9,44,5,3,9)
a=sorted(t)
print(a)