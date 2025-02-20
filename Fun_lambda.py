# add = lambda x,y:(x+y)
# p=eval(input("Enter number:"))

# q=eval(input("Enter number:"))
# print(add(p,q))




# add = lambda x,y:print(x+y)
# p=eval(input("Enter number:"))

# q=eval(input("Enter number:"))
# (add(p,q))


#Evan or odd
# number= lambda x:'even-no' if x%2==0 else 'odd number'
# p=int(input("enter number:"))
# print(number(p))



# positivee,nagitive,zero
# check_num=lambda x:'+ve' if x>0 else '-ve' if x<0 else 'Zero'
# p=int(input("Enter number:"))
# print(check_num(p))



# x=lambda p:[item for item in range(p)]
# p=int(input("number:"))
# print(x(p))


x=lambda p,q:[[r for r in range(p)] for i in range (q)]
p=eval(input("number:"))
q=eval(input("number:"))
print(x(p,q))