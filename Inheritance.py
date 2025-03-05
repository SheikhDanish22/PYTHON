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

class GP:
    def home(self):
        print("GP")


class P(GP):
    def Car(self):
        print("P car")


class C(P):
    def new(self):
        print("C")

obj=C()
obj.new()
obj.home()
obj.Car()