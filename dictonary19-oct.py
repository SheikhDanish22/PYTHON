#  Dictonary ---1-it is a mapping data type in which each element is represented as key value 
#pair.
#2-it is a mutable data (set)
#3- it is a orderd data type.
#4- element first inserted fatch.
#5- if we itereate a dictonary using for loop then data must be fetched in the order , in which
# it has been inserted
# reprasention of dictonary
d= { 1:"monday",2:"tuesday",3:"wednesday"} 
print(d)
print(d[1])
# print("\n")
print(d[2])
d[4]="thusday"
d[5]="friday"
print(d)
d[1]="sunday"
print(d)
d.update({1:"moday"})
print(d)

#property of key:
'''
1-key should be uniqe
2-if key are two then key take current data old data delete.
3- key must be consist of immutable data type. list/string/int/float/tupple
'''
#proprty of value:
'''
1- value can be duplicate
2- value can be consist of any data-type,
'''
d1={ 6:"saturday"}
d.update(d1)
d1={7:"sunday"}
d.update(d1)
print(d)

#21-oct
'''
    list as a value in dictionay
    dictionary as a value in dictionary

'''


# d={1:["ajay",23,"bhopal"],2:["vikas",24,"ujjain"]}
# print(d)
# d[2][2]="indore"
# print(d)

# d1={1:{"name":"ajay","age":23,"city":"bhopal"},
#     2:{"name":"jay","age":23,"city":"ujjain"}}
# print(d1)
# # d1[2][2]="indore"
# # print(d1)
# d1[2].update({"city":"indore"})
# print(d1)



#method of dictonary

# d={1:"mon",-2:"tue",3:"wed"}

# #keys()
# keys=sorted(d.keys())
# print("key=",keys)
# print(type(keys))

# #values()
# val=sorted(d.values())
# print("value=",val)
# print(type(val))

# #items()
# item=sorted(d.items())
# print("both=",item)
# print(type(item))

# #22-0ct
# # zip() method
# names=["Ajay","vikas","Arun","sonam","mandeep"]
# Age=[23,45,23,56,31,44]
# result=tuple(zip(names,Age))
# print(result)
# result=dict(zip(names,Age))
# print(result)

#get() ---- return value
# data = {'Ajay':23,'Vikas':34,'Arun':45}
# a=data['Arun']
# print(a)
# b=data.get('Shubham')
# print(b)

#setdefault()
# 1) Key available---> return existing value
# 2) key not available ---> key-value pair add return added value.


# data ={'1':2367,'2':2345,'3':3456}
# value=data.setdefault('4',23457)

# print(data)
# print(value)


#pop()
# data ={'1':2367,'2':2345,'3':3456}
# print(data)
# value = data.pop('2')
# print(data)
# print(value)



#popitem
# data ={'1':2367,'2':2345,'3':3456}
# print(data)
# data.popitem()
# print(data)


#clear()
# data ={'1':2367,'2':2345,'3':3456}
# print(data)
# data.clear()
# print(data)

data ={'1':2354,'2':3456,'3':4567,
       '4':{'11':3456,'22':63634,'44':4574}}


print(type(data)['1'])
data['4'].popitem()
print(data)