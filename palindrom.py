#palandrom nuos while
#112211==>112211
#nayan==>nayan
num=int(input("enter the value of num:"))
temp=num
r=0
sum=0

while num>0:#121
	r=num%10
	sum=sum*10+r
	num=num//10

if temp==sum:
	print("number is a pallindrom number")
else:
	print("number is not a pallindrom number")

##amstrong Nos
#371==>3**3+7**3+1**3==>27+343+1=371
#1634==>1**4+6**4+3**4+4**4==>1634
n=input("enter the value of num:")#153='153'
num=int(n) #int('153') ==>convert into int=153
temp=num #==>153
x=len(n)#==>3
r=0
sum=0
while num>0:#121
	r=num%10
	sum=sum+r**x
	num=num//10

if temp==sum:
	print("number is amstrong number")
else:
	print("number is not a amstrong number")