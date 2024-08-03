##the pattern of key value pair
#mh-31 gadchiroli
#mh-49  rural
#mh-33  bhandara
#mh-27  wani
#mh-34  chandrapur
#mh-32  gondia
d={"mh-31":"gadchiroli","mh-49":"rural","mh-33":"bhandara","mh-27":"wani","mh-34":"chandrapur","mh-32":"gondia"}
print(d)
##redandant value is allow in key value pair
dd={"mh-31":"gadchiroli","mh-49":"gadchiroli","mh-33":"bhandara","mh-27":"wani","mh-34":"chandrapur","mh-32":"gondia"}
print(dd)
##redundant key is not allow in key value
ddd={"mh-31":"gadchiroli","mh-31":"nandurbar","mh-33":"bhandara","mh-27":"wani","mh-34":"chandrapur","mh-32":"gondia"}
print(ddd)
print(ddd["mh-33"])
##important:-u can use duplicate value but not key in the key value pair.
##
r={101:"sagar",102:"yash",103:"piyush",104:"bittu"}
print(r)
r[105]="vipin"
def m1(): 
    a=10
    print(m1()) 
a=10
b=10
print(a!=b)
l1=[10,20,30,40]
l2=[10,20,30,40]
print(id(l1))
print(id(l2))
print(l1==l2)
print(l1 is l2)
print(bin(10)) #00001010
               #11110101
               #      +1
               #-----------
               #11110101(use 1st compliment)
               #00001010
               #00101000
               #      +1
               #-----
a,b=10,20 
x=30 
if a<b else 40 
print(x) #30 
c,d=20,30
d=50
if c<d  else 50
print(x)


