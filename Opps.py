# # # OPPS ------ kisi ak object ki multipal property or behaivour ko declare karna

# # # class ---- blue print of an object.
# # # object --- 
# # # self -- current class ke cureent refrens ko hold karta hai

# # #class basic sentex---

# # # class class_name:
# # #     "doc string"

# # #      constructor(optional)

# # #      variable

# # #      metods

# # #obj= class_name

# # # class student:
# # #     "Studnet Information"
# # #     name="Aman"
# # #     age=27
# # #     def add(p,q):
# # #         return p+q
# # # # print(dir(student))    #--init__ megic ya dindar method   
# # # # print(student.__doc__) 
# # # # print(student.__dict__)

# # # obj=student
# # # print(obj)
# # # print(obj.name)
# # # print(obj.age)
# # # x=obj.add(5,6)
# # # print(x)

# # # class Stutent:
# # #     "Std Info"
# # #     name="Aman"
# # #     age=27
# # #     def __init__(self):
# # #         print(id(self))
# # #         print("Constructor called.....")
# # #     def add(p,q):
# # #         return p+q    
# # # obj= Stutent()
# # # print(id(obj))



# # class Stutent:
# #     "Std Info"
    
# #     def __init__(self,name,age):
# #         self.name= name #instence--- esa variable jo apni values object badlane ke sath change kar de
# #         self.age= age
        
        
        
# #     def Show_det(self):
# #         print(self.name)
# #         print(self.age)   
# # obj = Stutent("Aman",27)
# # obj.Show_det()
# # obj1 =Stutent("Rahul",28)
# # obj1.Show_det()


# # # declaraton of instance Variable
# # #1) In Constructor
# # #2) In Instance methods
# # #3) Thorugh object (outside of the class)


# # '''

# # declartion of instance variable
# # 1) inside class 
# #               through constructor
# #               through intance method

# # 2) outside class 
# #              through object

# # calling  
# #    inside class 
# #              used self
# #              1) constuctor
# #              2) instance method
# #    outside class
# #              1) use object                                     


# # '''

# # class Student:
# #     def __init__(self,name,age):#declaration
# #         self.name=name  # declaration
# #         self.age=age
# #         print(self.name) # calling
# #         print(self.age)
# #     def add(self,school):
# #         self.school=school

# #     def show_det(self):
# #         print(self.name) # calling
# #         print(self.age)  # calling
# #         print(self.school) # calling
# #         print(self.city) # calling
# # obj=Student("Neeraj",37)
# # obj.add("Shs")
    
# # print("Outside=",obj.name)        
# # obj.city="bhopal"
# # obj.show_det()
        
#  # static  variable ---- ese variable jo object dependent nahu hote hai
#  #  declare---
#  #        inside class
#  #                   1) out-side method
#  #                   2) in-side method
#  #                   3) inside instance method
#  #       outside class       

# # class Student:
# #     "Student Information"
# #     school = "SHSC"                         # declaration of static variable in side class but outside of the mehtod.......
# #     def _init_(self,name,age):
# #         self.name = name
# #         self.age = age
# #         Student.city = "Bhopal"             # declaration of static variable inside constrctor.......
        
# #     def add_detail(self):
# #         Student.school_code=101             # declaration of static variable inside instance method.......

        
# # obj = Student("Neeraj",37)
# # Student.principal = "Indra Bahadur"        # declaration of static variable.......

        

# class Student:
#     "Student Information"
#     school = "SHSC"                         # declaration of static variable in side class but outside of the mehtod.......
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Student.city="Bhopal"             # declaration of static variable inside constrctor.......
#         print("Calling inside of Constructor = ",Student.school)               # calling of static variable.......
#     def add_detail(self):
#         Student.school_code=101             # declaration of static variable inside instance method.......
#         print("Calling inside of instance method = ",Student.school)               # calling of static variable.......
#         print("Calling inside of instance method = ",Student.city)                 # calling of static variable.......
#     def show_detail(self):
#         print(Student.school)
#         print(Student.city)
#         print(Student.school_code)
#         print("Calling inside of instance method = ",Student.principal)
        
# obj = Student("Neeraj",37)
# print("My_City=",Student.city)
# print("My_School=",Student.school)
# obj.add_detail()
# print("School_code=",Student.school_code)
# Student.principal="Indra Bahadur"        # declaration of static variable.......
# obj.show_detail()        



# x=50
# class Student:
#     x=10
#     def add():
        
#         print("add=",x)
#         y=20
#         print("y:",y)
#     def add1():
#         print("x",x)
# obj=Student
# obj.add()      
# obj.add1()
# print("Global=",x)



x="Danish"
class abc:
    #global x
    x="Aditya"
    def add():
        print("x=",x)
        y="Arun"
        print("y=",y)
    def add1():
        print("x3=",x)
obj= abc
obj.add()
obj.add1()
print("Global=",x)        