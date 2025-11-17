
# tuple_1=(12,55,11,525,1)
# print(tuple_1)
# i=0
# maxn=0
# l=len(tuple_1)
# print(l)
# while(i<len(tuple_1)):
#     if tuple_1[i]>maxn:
        
#         maxn=tuple_1[i]
#     i = i + 1

# print(maxn)

# tuple_1=(12,55,11,525,1)
# print(tuple_1)
# i=0
# l=len(tuple_1)
# print(l)
# minn=tuple_1[0]
# while(i<len(tuple_1)):
#     if tuple_1[i]<minn:
       
#         minn=tuple_1[i]
#     i = i + 1

# print(minn)
    


# tuple_2=(1,2,3,4,5)
# sum_t=0
# i=0
# while(i<len(tuple_2)):
#     sum_t=sum_t+tuple_2[i]
#     i = i + 1

# print(sum_t)

#questions to solve

# tuple_2=(12,13,34,2,1,78,0)
# evencount=0
# oddcount=0
# zerocount=0
# for i in tuple_2:
#     if i==0:
#         zerocount+=1
#     elif i%2==0:
#         evencount+=1
#     else:
#         oddcount+=1


# print(evencount)
# print(oddcount)
# print(zerocount)


# tuple_3=(100,100,11,99)
# n=0

# secondl=0
# for i in tuple_3:
#     if i>n:
#         n=i

#         for j in tuple_3:
#             if j < n and j > secondl:
#                 secondl = j

# print(n)
# print(secondl)

# tuple_3=sorted(tuple_3)

# lt=len(tuple_3)-2
# print(tuple_3[lt])


# tuple_4=(1,2,3,4,5)

# lt=len(tuple_4)

# sum=0
# for i in tuple_4:
#     sum+=i
    
# avg=sum/lt
# print(avg)

# tuple_5=(22,35,35,1,90)
# target=35
# countt=0
# for i in tuple_5:
#     if i==target:
#         countt+=1

# print(countt)
# isans = True
# tuple_6 = (1, 11, 2, 3, 4, 5)
# for i in range(len(tuple_6) - 1):
#     if tuple_6[i + 1] <= tuple_6[i]:
#         # print(i)
#         isans = False
#         break

# print(isans)


# 6. Reverse a Tuple (without using reverse function)
# python
# Copy
# Edit
# # Example: tuple_1 = (1, 2, 3, 4)
# # Output: (4, 3, 2, 1)

# tuple_7=(22,4242,655,233,67)

# print(tuple_7[::-1])
# i=len(tuple_7)-1
# while(i>=0):
#     print(tuple_7[i])
#     i-=1


# 7. Find the Product of All Elements in a Tuple
# python
# Copy
# Edit
# # Example: tuple_1 = (1, 2, 3, 4)
# # Output: 24


# tuple_8=(1,2,32,442,32)
# product=1
# for i in tuple_8:
#     product*=i


# print(product)



# 8. Find Numbers Greater Than a Given Number
# python
# Copy
# Edit
# # Example: tuple_1 = (2, 6, 3, 8, 1)
# # Given number = 4
# # Output: 6, 8


# tuple_9=(24,424,5456,232)
# gn=400

# for i in tuple_9:
#     if i>gn:
#         print(i)




# 9. Remove Duplicates from Tuple (convert to tuple again)
# python
# Copy
# Edit
# # Example: tuple_1 = (1, 2, 2, 3, 3, 4)
# # Output: (1, 2, 3, 4)


# tuple_10=(43,3,3,12,45,652)
# tuple1=[] #this is form of list empty list
# for i in tuple_10:
#     if i not in tuple1:
#         tuple1.append(i)
# tuple1 = tuple(tuple1)
# print(tuple1)



# 10. Get Index of a Specific Element
# python
# Copy
# Edit
# # Example: tuple_1 = (10, 20, 30, 40)
# # Find index of 30
# # Output: 2


# tuple_11=(33,42,24,4535)
# fin=24
# for index,i in enumerate(tuple_11):
#     if i==fin:
#         print(index)





# tuple_11 = (33, 42, 24, 4535)
# fin = 24

# for index in range(len(tuple_11)):
#     if tuple_11[index] == fin:
#         print(index)

        
# #  Even Numbers Sum
# numbers=[1,2,3,4,5,6]
# total=0
# for i in numbers:
#     if i%2==0:
#         total+=i


# print(total)

# # Reverse a String

# string="Manthan"

# print(string[::-1])

# # Count Word Frequency
# sente="python is fun and python is easy"
# sente=sente.split()
# print(sente)
# word_count={}
# for i in sente:
#     if i in word_count:
#         word_count[i]+=1
#     else:
#         word_count[i]=1


# print(word_count)

# # Palindrome Check

# def is_palindrome(word):
#     word=word.lower()
#     if word==word[::-1]:
#         return True
#     else:
#         return False
    

# print(is_palindrome("Level"))

# # Find Maximum Number

# def find_max(number_list):
#     return max(number_list)

# number_list=[232,34,922,31]
# print(find_max(number_list))


# # Remove Duplicates

# num_list=[1, 2, 3, 2, 1, 4]
# new_empty_num=[]

# def new_func(num_list, new_empty_num):
#     for i in num_list:
#         if i  not in  new_empty_num:
#              new_empty_num.append(i)
#     return new_empty_num

# new_empty_num = new_func(num_list, new_empty_num)
    
    
# print(new_empty_num)


# # Factorial using Loop

# number=5
# facto=1

# for i in range(1,number+1):
#     facto*=i

# print(facto)


# # Count Vowels

# word= "education"
# vowels=["a","e","i","o","u"]
# word=word.lower()
# count=0
# for i in word:
#     if i in vowels:
#         count+=1

# print(count)

# # Second Largest Number

# number_list=[1,2,3,5,24,55]
# duclipcate_list=number_list.copy()
# number_MAX=duclipcate_list.remove((max(duclipcate_list)))
# second_max=max(duclipcate_list)
# print(second_max) 
# print("original list",number_list)


# # Prime Number Check
# number_n=7
# count=0
# for i in range(1,number_n+1):
#     if number_n%i==0:
#         count+=1


# print(count)
# if count==2:
#     print("prime")
# else:
#     print("not prime")

# names = ["Alice", "Bob", "Charlie", "David", "jacob", "Jasmine", "Eve", "jack"]
# filtered_names=[]
# for i in names:
#     uname=i.lower()
#     if uname.startswith("j"):
#         names=i.upper()
#         filtered_names.append(names)

# print(filtered_names)


# def read_first_line(filename):
#     try:
#         f=open(filename,'r')
#         # print(f)
#         content=f.read()
#         print(content)
#         f.close()
#     except:
#         print("Error: File not found.")


# read_first_line("tes.txt")

user_input = "  PyThOn|iS|FuN \n"
user_input = user_input.lstrip().rstrip("\n").replace("|"," ").lower()

print(user_input)







