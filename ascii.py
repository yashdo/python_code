##Asciii codes
#A(65)
#AB
#ABC
#ABCD 
#ABCDE
num=int(input("enter the value of num:="))#5
for i in range (65,75):#65,.......69
	for j in range(65,i+1):#65,66,67,68,69
		print(chr(j),end=" ")#A
		print()

for i in range(num): #5
	for j in range(i+1): #0,1,2,3,4
		print(chr(65+j),end=" ")
		print()

for i in range(num): #range(5)--> 0,1,2 3,4,5
	print(" "*(num-i-1),end=" ") #" "*(5-1-1)=>" "*3
	for j in range(i+1):#range(1+1)==>range(2)==>0
		print(chr(65+j),end=" ") #chr(65+1)====>chr(66)==>a b
	print()
#inverse
for i in range(num): #range(5)--> 0,1,2 3,4,
	print(" "*(i+1),end=" ") #(" "*(0+1),end="")
	for j in range(num-i-1):#range()==>range(2)==>0
		print(chr(65+j),end=" ") #chr(65+1)====>chr(66)==>a b
	print()

#hollow Diamond
	
	