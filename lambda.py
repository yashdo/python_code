l=[1,2,3,4,5]
l1=list(map((lambda x:2*x),l))
print(l1)
l2=list(map((lambda x:x*x),l))
print(l2)

from functools import *
l=(1,2,3,4,5)
l1=reduce((lambda x,y:x+y),l))
print(l1)
l2=reduce((lambda x,y:x*y),l))
print(l2)


def wish(name):
	print(name,"good morning")
	return 1000

greeting = wish
print(greeting("sudhir"))
print(wish("sudhir"))
del greeting 

def outer():
	print("yash learning python")
	def inner():
		print("yash teaching python")
		print("yash is unable to teach and learn anything")
		inner()
outer()


