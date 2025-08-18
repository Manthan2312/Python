# list1=[1232,32323,31,311]
# print(type(list1))


# tuple=(223,2232,542,3467)
# print(type(tuple))

set1={12,13,11,11}
#print(type(set1))


set2={"MANTHAN","KHUSHBU"}
print(set1.union(set2))

set1.update(set2)

print(set1,set2)



set3={"Pretty little baby","lion","camel"}
set4={12,23,5,"lion"}
# print(set3.intersection(set4))
# set3.intersection_update(set4)
# print(set3,set4)


# print(set3.symmetric_difference(set4))
# set3.symmetric_difference_update(set4)



print(set3.difference(set4))

set5={3,2,1,43,2326,7}
set6={6,64,2,76,454}
print(set5.isdisjoint(set6))  #if common value exits return false and else true  

print(set5.issuperset(set6))  