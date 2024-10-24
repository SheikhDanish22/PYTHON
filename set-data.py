# SET ---  
'''set is a container in which we contain multipal data but duplication  is not allowed 
and unordered data type where our main concern is data , but not any order related to it,
then we use set.   symbol{ 1,2,3,4,5,6,7,8}

union ---  dono ko jod ke {1,7,9,3,2,5,99,11}
intersection----  jo dono mai common hai {3,2,5}
a-b =  set defrence {1,7,9}
b-a = set defrence {99,11}
'''

# a={1,3,9,9,7,2,5}
# b={2,3,99,11,99,5}
# c={1,33,7}
# print(a,b)


# s1={1,2,3,3,4,9,11,17}
# s2={4,5,9,17,89}
# s3={"a","b",1,2,3,88}
# print(s1)
# r=s1.union(s2,s3)

# r=s1|s2|s3
# print(r)
# j=s1.intersection(s2,s3)
# j=s1 & s2 & s3
# print(r)

#s1 ={'a','a','b','f','y','t'}
#s2 ={'b','y','1','6','7'}

# s1-s2 = {'a','y','1','6','7'}


# s1 ={1,2,3,3,4,9,11,17}
# s2 ={34,55}
# s1.update(s2)
# print(s1)

s1 ={1,2,3,3,4,9,(2,90,99),11,17}
s1.add((2,90,99))
print(s1)






