#function 
#syntax def fun_name():
	#build in function  int() find()  append()   ad()
	#user Define Function
print("=========================show==============================")
def show():  #non parameterized(Zero Arguments) #its printing only your message
	print("hellow good morning students") #function Defination
show() #function calling

def show(name):  #non parameterized(with arguments)
	print("hellow good morning",name) #function Defination
show("students") #function calling

print("===take a input From String inside the show function======")
name=input("enter the name")
def show(name):  #non parameterized(with arguments)
	print("hellow good morning",name) #function Defination
show("sagar") #function calling

print("==============factorials======================")
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
factorial(5)
factorial(25)
factorial(15)

print("=======oddeven with def function==============================")
def oddeven(num):
    if num%2==0:
        print("no is even")
    else:
        print("no is odd")
num=int(input("enter the no :"))
oddeven(num)


print("==============add three nos with def function====================")
def add(a,b,c):
    d=a+b+c
    return d
print(add(10,30,20))
print("=======matamatical calculation of two nos by multiple mathamatical operators nos=============================")
def add(a,b):
	sum=a+b
	sub=a-b
	mul=a*b
	div=a/b
	return sum,sub,mul,div
print(add(100,50))
p,q,r,s=add(60,20) #(30,40,1200,3.0)
print("addition",p,"substraction",q,"multiplication",r,"division",s)

print("==============keyword aargument==============")
def wish(name,msg):
	print(name,msg)

wish("sudhir",msg="good morning")
wish(name="sudhir",msg="good morning")
wish("monty","good morning")

print("=============default aargument==================")
def wish(addr,msg,name="yash"):
	print(name,msg,addr)

wish("Nagpur",msg="good morning")
wish(msg="good morning",addr="pune")
wish("nagpur","good morning")

print("=================addd multiple elements in function==========")
def add(*n):
	total=0
	for num in n:
		total=total+num
		print(total)

add(10,20,30,40,50)
add(10,20)
add(30,50,70)
add(10)
print("==========mix def===============")
def mix(name,*s,addr,age=12): #(positional,all,------,key=value)
	print("name",name)
	print("age",age)
	print("addr",addr)
	print(s)
mix("sudhir",10,20,30,'soft','sudhir',addr="Nagpur")

print("====key value in mix==========")
def mix(**n):
	for k,v, in n.items():
		print(k,v,end=" ")
mix(name="yash",age=18,add="nagpur")
print()


print("=======global and local=================")
a=10 #local
def add():
	global b #global
	b=20
	print(a+b)

def sub():
	print(a+b)
add()
sub()

#syntax of lambda function : lambda argument list: expression
def add(a,b):
	c=a+b
	return c

print(add(10,20))

print("==============lambda function===================")
s=lambda a,b:a+b
print(s(30,60))
print("======key aarguments ===========")
def wish(name,age,place="nagpur"):
	print(place,name,age)
wish(23,"sagar")
print("=======add multiple element=========")

print("==local and public============")
a=10 #local
def asub():
	global b
	b=12
	print(a-b)

def mul():
	print(a*b)
sub()
mul()


