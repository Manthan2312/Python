# # Find the second largest number in a list (without using max() twice).
# number_list=[11,411,432,717,84]
# number_list.sort()
# print(number_list[len(number_list)-2])

# maxn=number_list[0]
# # print(number_list[0])
# for i in number_list:
#     if i>maxn:
#         maxn=i
# print(maxn)
# number_list.remove(maxn)
# maxn=number_list[0]
# for j in number_list:
#     if j>maxn:
#         maxn=j
# print(number_list)
# print(maxn)

# maxn=number_list[0]
# new_list=[]

# for i in number_list:
#     if i>maxn:
#         maxn=i

# for j in number_list:
#     if j==maxn:
#         continue
#     new_list.append(j)


# maxn=new_list[0]
# for k in new_list:
#     if k>maxn:
#         maxn=k

# print(maxn)






# 👉 Find all pairs in a list whose sum is equal to a given target.

# numbers = [2, 4, 4, 1, 5, 1]
# target = 6

# pairs = set()

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             pairs.add(tuple(sorted((numbers[i], numbers[j]))))

# print(pairs)

# i=0

# pairs = set()
# while(i<len(numbers)-1):
#     if numbers[i]+numbers[i+1]==target:
#         # print((numbers[i],numbers[i+1]))
#         pairs.add(tuple(sorted((numbers[i], numbers[i+1]))))
#     i+=1

# print(pairs)
        

# 👉 Check if a string is a palindrome.

# example_str="Manthan"
# example_str=example_str.lower()
# print(example_str)

# re_example = "".join(reversed(example_str))
# print(re_example)
# print("Palindrome" if example_str == re_example else "Not a palindrome")


# 👉 Problem: Count the frequency of each character in a string

# words="eye"


# freq_dict = {}
# for char in words.lower():
#     if char in freq_dict:
#         freq_dict[char] += 1
#     else:
#         freq_dict[char] = 1


# print(freq_dict)




# 👉 Find all unique elements in a list and print them in sorted order.
# numbers = [4, 2, 7, 4, 2, 9, 1, 7]
# number_u=[]
# for i in numbers:
#     if i not in number_u:
#        number_u.append(i)

# number_u=sorted(number_u)
# print(number_u)



# 👉 Check if two strings are anagrams of each other.
# str="Dormitory"
# str1="Dirty room"

# str=str.lower().replace(" ", "")
# str=sorted(str)
# print(str)

# str1=str1.lower().replace(" ", "")
# str1=sorted(str1)
# print(str1)


# print("anagrams") if str==str1 else print("not") 


# 👉 Check if a number is prime or not.

# number=2
# count=0
# for i in range(1,number+1):
#     if number%i==0:
#         count+=1


# print("prime number") if count==2 else print("Not a prime number")




# for number in range(1, 101):
#     count = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             count += 1
#     if count == 2:
#         print(number)



# 👉 Day 8 Problem: Generate the Fibonacci sequence up to n terms.

# a = 0
# b = 1
# number = 7
# print(a)
# print(b)
# for i in range(2, number):
#     fib = a + b
#     print(fib)
#     a = b
#     b = fib


# 👉 Day 9 Problem: Find the factorial of a number

# number=5
# facto=1
# for i in range(1,5+1):
#     facto*=i


# print(facto)



# Find the largest element in a list without using max().

Input = [3, 7, 2, 9, 5]
maxn=Input[0]

for i in Input:
    
    if i>maxn:
        maxn=i


print(maxn)


Input = [3, 7, 2, 9, 5]
maxn = Input[0]
index = 0

for i in range(len(Input)):
    if Input[i] > maxn:
        maxn = Input[i]
        index = i

print("Largest:", maxn)
print("Index:", index)
