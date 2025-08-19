list_example=[1,3,4,5]

# sqaure_list=[]

# for i in list_example:

#     sqaure_list.append(i*i)

# print(sqaure_list)

def cube(x):
    return x*x*x

data=map(cube,list_example)
print(list(data))



new_empcode=[101,102,103,104]
data=filter(lambda x:x>101,new_empcode)
print(list(data))

from  functools import reduce



name=[1,2,3,4,5]

data=reduce(lambda x,y:x+y,name)

print(data)



number_list_marks=[45,24,63,42,45,24]


new_marks=[]
for i in number_list_marks:
    if i not in new_marks:
        new_marks.append(i)


print(new_marks)


name=["Manthan","Tiya","TD","Khushbu"]

data=filter(lambda x:len(x)>5,name)
print(list(data))