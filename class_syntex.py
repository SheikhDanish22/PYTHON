
#doc string print

class Student:
    "stu_deatils"
    name="Aman"
    quali="Mtac"
print(dir(Student))
print("Doc=",Student.__doc__)    
print(Student)#__main__
#python ka object
obj=Student
print(obj)#__main__

#class ka object
obj=Student()
print(obj)