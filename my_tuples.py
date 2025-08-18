print("Tuple")


my_tuple=(1,2,3)
print(my_tuple)
my_tuple=(1,"Manthan",23.12,-1,False)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])# -1 meaning is my_tuple.len()=5 so 5-1 =4 index element  answer is false

person=("Manthan",23,"CEO")
Name,Age,Position=person
print(Age)
print(Name)
print(Position)
print(person)


my_class=[("Amit",23),("Manthan",23),("Tirth",22)]
print(my_class)
for name,age in my_class:
    print(name)
    print(age)

tuple1=(12,3,1)
print(tuple1)
#tuple[0]=123    #tuples are Immutable
print(tuple1[0])

length=len(tuple1)
print(length)
print(12 not in tuple1)

singlet=(123,)   
print(type(singlet))  #if you remove the , from the tuple that type it show as a int type if you want the stay as a tuple type put the , for one word

#methods of the tuples 

tuple=(23,5,12,"Manthan","Khushbu",True)
print(len(tuple))
tuple=(1,54,232,12,-7)
print(max(tuple))
print(min(tuple))
print(sum(tuple))

del tuple  # This deletes your overwritten variable and restores the built-in function
s = "hello"
print(tuple(s))  # ✅ Works again: ('h', 'e', 'l', 'l', 'o')


t = (1, 2, 2, 3, 2)
print(t.count(2))  # Output: 3


t = ("a", "b", "c", "b")
print(t.index("b"))  # Output: 1

a=(1,2,3,"Manthan","Khushbu")
a=list(a)
print(a)

a.append(23512)
a.remove("Manthan")
a[1]=10


a=tuple(a)
print(a)


l = [1, 2]
l.append([3, 4])   # l becomes [1, 2, [3, 4]]
# vs
l = [1, 2]
l.extend([3, 4])   # l becomes [1, 2, 3, 4]


# Original tuple
t = (1, 2, 3)

# Convert to list
l = list(t)

# Add items from another iterable (e.g., another list or tuple)
l.extend([4, 5])
# You can also use a tuple: l.extend((6, 7))

# Convert back to tuple
t = tuple(l)

print(t)  # Output: (1, 2, 3, 4, 5)
