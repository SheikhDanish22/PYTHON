x=10
def show():
    global y
    y=20
    x=50
    print("Globals=", globals()['x'])
    print(y)
    
show()
print(x)
print("globale=",y)
   
