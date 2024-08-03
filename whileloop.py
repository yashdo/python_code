#while looop
#while condition:
i=1
while i<=10:  #1<=10 (True)
	print(i,end=" ") # 1 2 3 4 -----10
	i=i+1 #10+1 ==>11 

i=1
while i<=50:  #1<=50 (True)
	print(i*5,end=" ") # 1 2 3 4 -----10
	i=i*5 #10+1 ==>11 


#reverse a nos
num=int(input("enter the number:=")) #786
r=0 
sum=0
while num>0:  #786>0 (True))
	r=num%10  #786%10==6
	sum=sum*10+r #0*10+6===>6
	num=num//10  #786//10==>78
print("my reverse number is :",sum)

#reverse a nos
num=int(input("enter the value of num:="))
r=0
sum=0
while num>0:
	r=num%10
	sum=sum*10+r
	num=num//10
print("return the reverse nos:=",sum)





