#tuple
'''
1. it is a sequence data type
2. ordered data type
3. it is immutable data type
4. a)we can representation ()
   b) comma seperated
5. it is faster then list
6. single element representation.
7. generally whenever data is fatched from database
  it is stored in the form of tuple or dictionary.
8. it is a container, which store multiple data objects.
'''

fruit=("apple",20,100)
print(type(fruit))
#fruit[2]=200 # error(immutable)
print(id(fruit))
print(id(fruit[0]),id(fruit[1]),id(fruit[2]))
fruit =("apple",20,100) + ("apple",20,100)
print(fruit)

# note---- 