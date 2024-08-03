#sets
l=[10,20,30,40,50] #list
print(type(l))
print(l) #[10,20,30,40,50]
s=set(l) #{10,20,30,40,50}
print(s) #{10,20,30,40,50}
print()  #next line
print("===========range()=======")
s=set(range(10))  #set{0,1,2,3,4,5,6,7,8,9}
print(s)

for x in s:
	print(x,end="")

print()
print("===============add()=========")
s1={"10,20,30,40,50"}
s1.add(10)
s1.add(20)
s1.add(30)
s1.add(40)
s1.add(50)
print(s1)
s1.add(100) #{"10,20,30,40,50,100"}
s1.add(200) #{"10,20,30,40,50,100,200"}
print()
print("====================update()==================================")
#you will update sets inside the list only by call first #sets.update(list)
#u can use update function with dict 
s={1000,} #Iterable-->list ,range(5),tuple
print(type(s))
l=[10,20,30,40,50]
print(type(l))
s.update(l,range(5),(100,300,400),"SOFTRONIX")
print(s) #{10,20,30,40,50,0,1,2,3,4}
print("=====================object cloning=======")
#there are tow same object and you want to modify perticular one in this case we are using cloning concept with copy and slicing operator
s={10,20,30,40,50}
s1=s.copy()
print(s)
print(s1)
s.add(100)
s1.add(1000)
print(s)
print(s1)

print()
print("====================pop()=========")
s={10,20,30,40,50}
print(s)
print(s.pop())
print()
print("=========remove(x)========") #its remove perticular element by given the 
s={10,20,30,40,50}
print(s)
print(s.remove(30))
print(s)
print()
print("=====to acess the object from sets=====")
s={10,True,10.5,10+20.4j,1,3,5,6,"soft"}
print(s)
def find():
	a=eval(input("enter your choice:")) #true
	for x in a:
		if x==a:
			print("a=",x)
print("========discrad(x)=========")
s={10,20,30,40,50}
print(s)
print(s.discard(30))
print(s)
print()
print("========clear=========")
s={10,20,30,40,50}
print(s)
print(s.clear())
print(s)
print()
print("==========union===========")
#return all data of sets except duplicates
s={10,20,30,40,50}
s1={70,80,90,100,10,20,30,40}
print(s.union(s1))
print(s)
print()
print("===============intersection===================")
#it return common from sets
s={10,20,30,40,50}
s1={70,80,90,100,10,20,30,40}
print(s.intersection(s1))
print(s)
print()


print("=====================take a string and find vovels present in that string====================")
s=set(input("enter the value of string"))
s1={"'a','e','i','o','u'"}
print(s1.intersection(s))
print()

print("===========difference=================")
#it return either entire data or common data expects duplicates from sets.
x={10,20,30,40,50,100,200,300}
y={10,20,30,40,50,1,2,3}
print(x.difference(y))
print(y.difference(x))

print("==============symmetric difference()===================")
#it will return only the unique value except duplicates value
x = {10, 20, 30, 40} 
y = {30, 40, 50, 60} 
print (x.symmetric_difference(y)) #{10, 50, 20, 60} 
print(x^y) # {10, 50, 20, 60} 
print("==============sets comprehension=================")
#it return either entire data or common data expects duplicates from sets.

