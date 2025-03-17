class P:
    x=10
    def home(self):
     print("P Home")

class C(P):
   def home(self):
      super().home()
      print("C home")

obj=C()
obj.home()

