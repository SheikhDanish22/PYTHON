'''single inheritace----  ak perent or ak child'''


# class P:
#     x=10
#     def home(self):
#         print("P home")

# class C(P):
#     y=20
#     def Car(self):
#         print("my car")

# obj=C()
# print(C.x)
# obj.home()
# obj.Car()
# print(C.y)



#method overriding
# class P:
#     x=10
#     def home(self):
#         print("P home")

# class C(P):
#     y=20
#     def home(self):
#         super().home()
#         print("my car")

# obj=C()
# obj.home()
# # print(C.x)
# # obj.home()
# # obj.Car()
# # print(C.y)


#method overloading

# class A:
#     def add(self,x,y):
#         print(x+y)
    
#     def add(self,x):
#         print(x)


#     def add(self,x,y,z):
#         print(x+y+z)


# obj=A()
# obj.add()
    

#Multipale 
#MRO--- method resulation order

# class P1:
#     def home(self):
#         print("P1")

    
# class P2:
#     def home(self):
#         print("P2")

# class C(P1,P2):
#     def Car(self):
#         print("car")

# obj=C()
# obj.home()



#Multileval

# class GP:
#     def home(self):
#         print("GP")


# class P(GP):
#     def Car(self):
#         print("P car")


# class C(P):
#     def new(self):
#         print("C")

# obj=C()
# obj.new()
# obj.home()
# obj.Car()



#Hierarchical Inheritance
# class P:
#     def home(self):
#         print("from P clss")

# class C1(P):
#     def home1(self):
#         print("from C1 clss")


# class C2(P):
#     def home2(self):
#         print("from C2 clss")

# obj=C1()
# obj.home()
# obj=C2()
# obj.home()



#Same Method hai to super() li help se Perent ko call kar sakte hai

# class P:
#     def home(self):
#         print("from P clss")

# class C1(P):
#     def home(self):
#         #print("from C1 clss")
#         super().home()

# class C2(P):
#     def home(self):
#         #print("from C2 clss")
#         super().home()

# obj1=C1()
# obj1.home()
# obj2=C2()
# obj2.home()



#Hybrid Inheritance

# class P:
#     def home(self):
#         print("P class")

# class C1(P):
#     def home(self):
#         print("C1")

# class C2(P):
#     def home(P):
#         print("C2")

# class C3(C1,C2):
#     def new(self):
#         print("C3")

# obj=C3()
# obj.home()
# print(C3.__mro__)




