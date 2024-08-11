l=[1,2,3,4,5,6,7,8,9,10]

def isEven(x):
	if x%2==0:
		return True
	else:
		return False

def isodd(x):
	if x%2!=0:
		return True
	else:
		return False

s=list(filter(isEven,l))
print(s)
h=list(filter((lambda x:x%2==0),l))
print(h)
s1=list(filter(isodd,l))
print(s1)



