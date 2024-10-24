# # string 
# # 1) sequence (ordered)
# # 2) immutable

# msg= "string is a immutable data-type"
# #msg[3]="y"
# print(msg[12:21])

# #methods of string

# msg= "string is a immutable data-type"

# #capitalize()   ---- capitalize string
# a=msg.capitalize()
# print(a)
# print(msg.capitalize())



# #upper function ---->

# msg= "string is a immutable data-type"
# b=msg.upper()
# print(b)


# # lower()


# msg= "String iS a immutable data-type"
# print(msg)
# c=msg.lower()
# print(c)

# # isupper ----> boolean output true/false

# msg= "string is a immutable data-type"
# d=msg.isupper()
# print(d)

# #islower -----> boolean output true/false

# msg= "string is a immutable data-type"
# e=msg.islower()
# print(e)


# #isdigit

# msg= "12123455"
# f=msg.isdigit()
# print(f)



# #isalfa

# msg= "stringisaimmutabledatatype"
# g=msg.isalpha()
# print(g)

# #replace("old value","new value") 

# msg= "string is aimmutable data type"
# g=msg.replace("is","Is")
# s=g.replace("a","b",2)
# s3=g.replace(g,"new")
# print(g)
# print(s)
# print(s3)

# #split()  -----> list return
# sp = "He is great person"
# sp1=sp.split('e',1)
# print(sp1)

# #join() -----> return string
# l =[" apple "," banana "," orange "," mango "]
# l1 =[ " fig " , " coconut "] #tuple bi likh sakte hai
# s="".join(l)
# s=" , ".join(l) +" ,   "+" , ".join(l1)
# print(s)

# strs = "its now or never"
# s=strs.split()

# print(s)
# a=s[0][::-1]
# b=s[1][::-1]
# c=s[2][::-1]
# d=s[3][::-1]
# s=[a,b,c,d]
# print(s)

s="Apple Banana"

a=s[6:]
print(a)
b=s[::1]
print(b)
c=s[6:]+" "+s[:5]
print(c)
