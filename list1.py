l=[10,20,30,40,50,60]
print('#'*20,"===========append()=========",'#'*20)
l.append(100)
l.append('A')
print(l)
print()
print()
print('#'*20,"===========insert()=========",'#'*20)
l1=[10,20,30,40,50,60]
l1.insert(1,1000) #10  1000 20 30 40 50 60
print(l1)
l1.insert(10,'A') # 0   1  2  3  4  5 6 ----> 10  1000 20 30 40 50 60 A
print(l1)
l1.insert(-10,'B')#-6  -5 -4 -3 -2 -1   -----> B 10  1000 20 30 40 50 60 A
l1.insert(-5,True)   #(-5+1=-6)
print(l1) #B  10  20 True 30 40 50 60 A 
l1.insert(5,100)   #B  10  20 True 30 40 50 100 60 A
print(l1)


print('#'*20,"===========extend()=========",'#'*20)
l2=[10,20,30]
l3=['A','B','C']
l4=["SOFTRONIX"] #--['S','O','F','T','R','O','N','I',X]
l5=["10+20.6j"]
l2.extend(l3)
l2.extend(l4)
l2.extend(l5)
print(l2) #[10,20,30,'A','B','C','S','O','F','T','R','O','N','I',X]

print()
print('#'*20,"===========remove()=========",'#'*20)
#remove element will remove perticular element from list
ls=['A','B','C','D','E','F','G']
ls.remove('C')
print(ls)

print()
print('#'*20,"===========pop()============",'#'*20)
lp=['A','B','C','D','E','F','G']
lp.pop() #G
lp.pop() #F
print(lp)#['A','B','C','D','E']

print()
print('#'*20,"===========reverse()========",'#'*20)
lr=['a','b','c','d','e','f','g']
lr.reverse() #['G','F','E','D','C','B','A']
print(lr)

print('#'*20,"===========sort()===========",'#'*20)
lss=[0,5,6,2,3,7,9,10,1,4,8]
lss.sort()
print(lss)
print('#'*20,"=====sort(reverse=True)=====",'#'*20)
lss.sort(reverse=True)
print(lss)

print("=====================Aliasing and Cloning of List Objects: duplicate copy================")
print("===================cloning============")

x=[10,20,30,40,50,60]
print(x)
y=x[:] #slicinng
print(y)
z=x.copy()
x[-1]=10000
print(y)
print(x)
print(z)
print(id(y))
print(id(y))
print(id(y))
print("=========split=========================")
s="Learning Python is very very easu launguage"
#if you are taking a string output for spliting value then it willl return the list datatype
l=s.split() 
print(l) 
print(type(l)) 

########
n = [0,1,2,3,4,5,6,7,8,9,10] 
i = 0 
while i < len(n): 
    print(n[i]) 
    i=i+1 
print("========clioning==============")
x=[10,20,30,40,50]
y=x[:] ##cloning with copy and slicing
x=y
print(id(x))
print(id(y))
y[1]='1000'
print(y)
print(x)
x[0]='50'
print(x)
print(y)
print(id(x))
print(id(y))
print("===============2nd cloning=======================")
x=[10,20,30,40,50]
y=x.copy()
print(id(x))
print(id(y))
print(x)
print(y)
y[1]='500'
print(y)
x[2]='1000'
print(x)
print("==================3rd cloning=====================")
x=[10,20,30,40,50]
y=x[:]
print(id(x))
print(id(y))
x[2]="-300000"
y[3]='5500000'
print(x)
print(y)
print("========concatenate and multimplication concept================")
a = [10, 20, 30] 
b = [40, 50, 60] 
c=a+b
print(c)
d=c+["yash ajay dollarwar"]
print(d)
##multiplication(it will return the list by given multiple nos)
a = [10,20,30] 
b = 2
c=a*b
print(c)
print("===============comparission operator============================")
##it will check the 1st element of list either it is numeric or textual doesent matter
x = [50, 20, 30] 
y = [40, 50, 60, 100, 200] 
print(x>y)   #true
print(x>=y)  #true
print(x<y)   #false
print(x<=y)  #False
x = ["Dog", "Cat", "Rat"] 
y=["Rat", "Cat", "Dog"]
print(x>y) #false
print(x>=y) #false
print(x<y)  #true
print(x<=y) #true
print("==============membership operator==============================n")
##(n) operator check the substring inside the main string
a=[10,20,30,"yash",40,50,60]
print(10 in a)   #true
print("yash" not in a)  #false
print("==============clear operator===============")
#it will clear means delete the entire list string 
n=[10,20,30,40,50,60]
print(n.clear())
print("=============nested list=======================")
a=[10,20,30,[40,50],[40,50,60],[100,200,300]]
print(a[3])
print(a[5][1])
print()
print("=============numpy as np for matrix====================")
import numpy as np
n=[[10,20,30],[40,50,60],[70,80,90]] 
v=np.array(n)
print(v)

print("====new way==============")
n=[[10,20,30],[40,50,60],[70,80,90]] 
for r in n: 
	print(r) 
      
print("===============list comprehension================================")
s = [ x*x for x in range(5,50)] 
print(s) 











