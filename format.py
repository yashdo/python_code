#formating 
name="rahul"
sal=50000.23
age=23
print("{}s salary is {} at athe age of{}".format(name,sal,age))
print("{2}s salary is {1} at athe age of{0}".format(name,sal,age))
print("{x}s salary is {y} at athe age of{z}".format(x=name,y=sal,z= age))
print()
print('#'*40)

print("the integer number=>{}".format(358))
print("the integer number=>{:d}".format(358))
print("the integer number=>{:3d}".format(358))
print("the integer number=>{:015d}".format(358))
print()
print('#'*40)

print("the integer number=>{0:b}".format(10))
print("the integer number=>{0:o}".format(10))
print("the integer number=>{0:x}".format(14)) #0,1---9,a=1,b=2,---g=16
print("the integer number=>{0:X}".format(10))

print("The float Number =>{}".format(358))
print("The float Number =>{:f}".format(358))
print("The float Number =>{:8.2f}".format(358.123))
print("The float Number =>{:8.3f}".format(35845.6))
print("The float Number =>{:025.5f}".format(53153354358.68975))
print("The float Number =>{:8.5f}".format(53153354358.68975))

print()
print('#'*40)
print("The float Number =>{:8.3f}".format(358454555555555.45666666))