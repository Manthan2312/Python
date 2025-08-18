"""
a=input("Enter your name:")
print(a)

a1=(int)(input("Enter Your First Number:"))
b1=(float)(input("Enter Your Second Number:"))
print("The Sum Of Enter Numbers are:",(a1)+(b1))
"""

name="ManthanPatel"

print(name[0]) 

print(name[0:3]) #ending 3-1  =2  

print(name[:5]) #detect automatically 0 index

print(len(name))

print(name[:len(name)]) 
#len(name) is behind for logic  the number you give automatically - from len(variable)

print(name[:-2])
#len(name) is behind for logic  the number you give automatically - from len(variable)
# len(name)=12  and 12-2: 10  [0:10]



print(name[-2:-3])
# in[] first is 0 . we see the logic behind that len(variable)-2  12-2 =10 
# 12-3=9   decode[10:9]  no make sense
#if we rev..  

print(name[-3:-2])# in[] first is 0 . we see the logic behind that len(variable)-3  12-3 =9 
# 12-2=10   decode[9:10]   make sense if decode[10:10] that time no make sense

nm="Harry"
print(nm[-4:-2])