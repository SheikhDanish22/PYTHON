# ''' 1) Sequancial
#    2) conditional
#                 1) if
#                 2) if-else
#                 3)if-elif
#                 4)if-elif-else
#    3)Iterative/looping
#                  1) while --- infinite time(increment or decriment nahi hoga)
#                  2)for

#   4) Transfar statement
#                 1)continue(keyword)
#                 2)brack(keyword)
#                 3)pass (keyword)


# ----------------------------------------------------------------------------------------------------
# flow chart :-
              
# x=10
# y=10
# if x==y:
# print("Equal")
# print("hello")        


# syntex:-

#    if(condition):
#    {
   
   
#    }

                
# '''
# # x=20
# # y=20
# # if x==y:
# #  print("Equal")
# # else: 
# #  print("hello")        




# # x=20
# # y=20
# # if x==y:
# #  print("Equal")
# # else:
# #  print("Hello")    

# # x=int(input("Enter one no= "))
# # y=int(input("Enter 2nd.no="))
# # print("1 Add\n 2.sub\n 3.Div\n 4.malti")

# # n=int(input("Enter or. ch="))
# # if n==1:
# #  print(x+y)
# # elif n==2:
# #   print(x-y)
# # elif n==3:
# #      print(x/y)
# # elif n==4:
# #      print(x*y)


# #While-loop
# '''syntax-
   
#    initialization
      
#    while condition:

#    incrment/decriment(i=i+1/i=i-1)   



# '''
# n=int(input("enput number="))
# i=2
# while i<=n:
#    if i%2==0:
#     if i<=(n-2):
#      print(i,end=',')  #infinite    #even number
#    else:
#       print(i)
      

      
#    i=i+2 #finite


# # n=int(input("Enter your number="))
# # i=1
# # while i<=n:
# #    if i<19:
   
# #       print(i,end=' ,')   #odd number
   
      
# #    else: 
# #     print(i)
# #    i=i+2


# # n=int(input("Enter your number="))
# # i=1
# # sum=0
# # while i<=n:
   

# #  print(i,end = ' + ')
# #  sum=sum+i
# #  i=i+1
# # print(" = ",sum)

# # n=int(input("Enter number="))
# # i=1
# # mul=1
# # while i<=n:
# #    print(i,end = ' * ')
# #    mul=mul*i
# #    i=i+1
# # print("=",mul)


# 
# 
# n=int(input("Enter numbe="))
# i=1
# while i<=n:
#       if i%2!=0:  #even number
#          if i<=(n-2):
#             print(i,end = ' , ')
#          else:
#             print(i)

         

#       i=i+1

# n=int(input("Enter numbe="))
# i=1
# sum=0
# while i<=n:
#       if i%2==0: 
#          sum=sum+i #even number sum
#          if i<=(n-2):
#             print(i,end = ' + ')
#          else:
#             print(i,end = ' = ')

#       i=i+1
# print(sum)     


 #n=int(input("Enter numbe="))
# i=1
# while i<=n:
#       if i%2!=0:  #even number
#          if i<=(n-2):
#             print(i,end = ' , ')
#          else:
#             print(i)

         

#       i=i+1

n=int(input("Enter numbe="))
i=1
sum=0
while i<=n:
         sum=sum+2*i
         if i<=n:
            
            print(2*i,end = ' + ')   #print even number /  odd 2*i-1(odd number)
         else:
            print(2*i, end = ' = ')

         i=i+1
   
