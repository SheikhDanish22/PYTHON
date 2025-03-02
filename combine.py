class Student:
    school='SHSS' #static variable
    def __init__(self,name,roll):
        self.x=name    #instance variable
        self.y=roll
    def new(self):
        x=10
        print("Local variable x:",x)
    def show(self):
        print(self.x,self.y)

obj=Student('danish',101)
obj.new()
obj.show()        