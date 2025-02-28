'''constructer --- 
con. is a spacial type of method that called automticlly when object create'''


# class Student:
#     def __init__(self):
#         print("Call Constructer")
#         print("self",id(self))

# obj=Student
# print(id(obj))



# obj=Student()# cunstructer call response ()
# print(id(obj))


# class Student:
#     def __init__(self,name,roll,marks):
#         self.x=name
#         self.y=roll
#         self.z=marks
# obj=Student("Danish",101,96)
# print(obj.x)
# print(obj.y)
# print(obj.z)
        


class Stu:
    def __init__(self,name):
        self.x="danish"

    def __init__(self):
        print("con")
obj=Stu()   # currnt ke constructer ko bulata hai 
obj.__init__() # constructer ko bahar call kar sakte hai
        
