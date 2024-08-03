#continue (continue statement will break the first itteration and continue next)
cart=[10,20,500,700,800,900,50,60] 
for i in cart: 
	if i>=500: 
		print("item is greater than 500 :") 
		print(i)
		continue
#write a programe to print 10 to 80 values by using range and output will be in between 10 to 80:
for i in range(10,80): #10,11,12,13,14,15,.............80
	if i>=10 and i<=30:  #10>=10 and 10<=30:(true) unless condition wont be false its going continue
		print("enter the value between 10 and 30:=",i)
		continue

numbers=[10,20,0,5,0,30] 
for n in numbers: 
	if n==0: #10,20,0,5,0,30
		print("Hey how we can divide with zero..just skipping") 
		continue 
	print(format(100/n)) #100/10,100/20,100/0,100/5,100/0,100/30
