
#Instance method 
# Constructor bi instance method hai 
# kuki dono mai self hota  hai.

# class A:
#     def new(self):           #declaration
#         print("!st method")
        
#     def new1(self):
#         self.new()            #calling
#         print("@nd method")
# obj=A()
# #obj.new()
# obj.new1()        




#class method:-
# cls keyword
# static var ki value ko modify karne ke liye class method ka use karte hai.
#@classmethod 

# class Book:
#     price=150  # static var
#     def __init__(self,Author,pages):
#         self.Author=Author
#         self.pages=pages
#     @classmethod
#     def update_price(cls,price):
#         cls.price=price
#     def show(self):
#         print(self.Author)
#         print(Book.price)
#         print(self.pages)
# obj=Book('Neeraj',500)
# obj.show()
# print("After")
# obj.update_price(250)
# obj.show()
# 
#                 


      