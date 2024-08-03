#break
for i in range(1,100,4): 
		print(i)
cart=[10,20,600,60,70] 
for item in cart: 
	if item>500: 
		print("To place this order insurence must be required") 
		break 
	print(item) 

#break statment we are using iside the loop:
for i in range(1,100):
	if i==26:
		print(i)
		break
#for commit the one condition inside the loop we are using break function
sales=[10,20,400,500,600]
for i in sales:
	if i>=300:
		print("to figer out sales greater than 300 premium required")
		print(i)
		break
amount=(100,200,300,400,500,600,700,800,100)
for i in amount:
	if i>=200:
		print("greater than 200 amount")
		print(i)
		break #(break operation we will perform when we required only single output in range)


