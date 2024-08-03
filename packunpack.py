print("#"*20,"---tuple packing and unpacking----","#"*20)
a=10
print(id(a))
b=20
print(id(b))
c=30
print(id(c))
d=40
print(id(d))

t=a,b,c,d
print(t)
print(id(t))
a,b,c,d=(100,200,300,400)
print(a,b,c,d,end="")
print()
a=[10,20,30]
b=40
c=50


tt=a,b,c
tt=(10,20,30)+(40,)
#tt[0]=[40,50,60]
print(tt)

t1=(10,20,30)
print(id(t1))
t1=(10,20,30,40)+(50,)
print(id(t1))
t1=(10,20,30,40)+([50,60,70])
print(t1)