d1={'name':'Danish','age':'28','quali':'Msc'}
# print(max(d1))
# print(min(d1))
# print(len(d1))
# print(type(d1))
# print(id(d1))

#clear()  method
# d1.clear()
# print(id(d1))



#copy()
# d2=d1.copy()
# print(d1,d2)


#fromkeys

# l2=['name','email','contact']
# d2=dict.fromkeys(l2)
# print(d2)
# d3=dict.fromkeys(l2,'danish')/////////////////////////////////////////////////////////////////
# print(d3)


# #get()
# d1={'name':'Danish','age':'28','quali':'Msc'}
# print(d1.get('name'))


# print(d1.keys())
# print(d1.values())
# print(d1.items())
# print(d1.popitem())
# print(d1)
# print(d1.pop('age'))
# print(d1)


#set 

d5={'name':'danish','age':'28'}
# d5.setdefault('name','danni')
# print(d5)
# d5.setdefault('new','Guest')
# print(d5)


#update()

d1={'id':'1'}
d1.update(d5)
print(d1)
