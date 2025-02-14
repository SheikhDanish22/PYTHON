# x=10  #global
# def add():
#     y=20   #local
#     print('global',x)
#     print(y)
# add()
# print('Global-',x)





# x=10
# def add():
#     global x
#     print(x)
#     x=20
#     print(x)

# add()
# print(x)


# x=10
# def new():
#     x=20
#     print('global',globals()['x'])
#     print('local',x)
# new()
# print(x)





x=10
def new():
    global y,z
    x=20
    y=30
    z=50
    print('global',globals()['x'])
    print('local',x)
new()
print(x)
print(y)
print(z)


