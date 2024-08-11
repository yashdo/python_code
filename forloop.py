num=int(input("enter the value of num:=")) #5
for i in range(1,num+1): #range(start,End)
	print("*" * num)

#2nd way of forloop 
num=int(input("enter the value of :="))
#===outer loop
for i in range(1,num+1):#1,2,3,4,5
	#----inner loop
	for j in range(1,num+1):#1,2,3,4,5,
		print("*",end=" ")
	print()

s="yash learning python in softronix"
s1=print(s[::-1])
s2=s1.split()
s3=s2.join()
print(s3)
