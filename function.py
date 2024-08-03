# function 
#syntax

def wish():  #function declaration
	print("yash learning python in softronix")  #fun define
wish() #function calling

#syntax 
#def fun name(para_list):
#a=10 b=20  a=20 b=10
#temp=a
#a=b
#b=temp
def swap(a,b):
	print("before swaping value of a=",a,"b=",b)
	a,b=b,a
	print("after swaping the value of a=",a,"b=",b)

swap(100,200)

#swaping 2nd logic
def swap(c,d):
	print("before swaping value of a=",c,"b=",d)
	c=c+d
	d=c-d
	c=c+d

	print("after swaping the value of a=",c,"b=",d)

swap(100,200)