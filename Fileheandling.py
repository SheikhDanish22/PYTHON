# f=open('n1.txt','r')
# print("name",f.name)
# print("mode",f.mode)
# print("True",f.readable())
# print("Write,",f.writable())
# print("close",f.closed)



# f=open('n1.txt','w')
# print("name",f.name)
# print("mode",f.mode)
# print("True",f.readable()) 
# print("Write,",f.writable())
# print("close",f.closed)


# f=open('p1.txt','a')
# data=['hello\n','hiii\n','sasriyakal\n']
# f.writelines(data)
# f.flush()
# f.close()



'''File read karna 
read()
'''
# f=open('n1.txt','r')
# data=f.read()
# print(data)


f=open('n1.txt','r')
# data=f.read(10)
# print(data)
# print(f.tell())
# data=f.readline()
# print(data)

# data=f.readlines()
# print(data)



'''
tell()----cursor position

seek()----- coror move 
     seek(where we move,move from )


'''




# f=open('n2.txt','w+')
# print(f.readable())

# print(f.writable())

# print(f.closed)


# f=open('n2.txt','r+')
# print(f.readable())

# print(f.writable())

# print(f.closed)

# f=open('n2.txt','a+')
# print(f.readable())

# print(f.writable())

# print(f.closed)




#   BINARY FILE
'''

img,audio,video (byte string mai)

source code ko byte code mai convert karne ke liye pickle(pickling) module karta hai hai

.bin , .dat , .pkl
'''
import pickle
# f=open('f1.dat','ab')
# data=[10,20,30,'danish']
# pickle.dump(data,f)
# f.close()


f=open('f1.dat','rb')
data=pickle.load(f)
print(data)

