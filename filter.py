# def even(x):
#     if x%2!=0:
#         if x>0:
#          return x
# l1=[-1,2,3,-4,5,6,7,8]
# res=filter(even,l1)
# print(list(res))    



# def even(x):
    
#         if x<0:
#          return x
# l1=[-1,2,3,-4,5,6,7,8]
# res=filter(even,l1)
# print(list(res))



# def even(x):
#     if x%2!=0:
    
#          return 'even'
#     else:
#          return 'odd'
# l1=[-1,2,3,-4,5,6,7,8]
# res=map(even,l1)
# print(list(res))




def res(x):
    if len(x)<=3:

     return x

l1=['Neeraj','Rahul','Raj','Jai']
r=filter(res,l1)
print(list(r))