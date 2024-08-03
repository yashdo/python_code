#list comprehension
l=[x*x for x in range(1,11)] #1*1,2*2
print(l)
print()
l1=[x**2 for x in range(1,11)]  #1**2,2**2
print(l1)
print()
t=(1,2,3,4,5,6,7,8,9,19)
l2=[x for x in t if x%2==0]
print(l2)
t=(10,20,30,40)
t1=(30,50,60,70)
t2=t+t1
print(t2) 