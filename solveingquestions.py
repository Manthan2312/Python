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

# Input = [3, 7, 2, 9, 5]
# maxn=Input[0]

# for i in Input:
    
#     if i>maxn:
#         maxn=i


# print(maxn)


# Input = [3, 7, 2, 9, 5]
# maxn = Input[0]
# index = 0

# for i in range(len(Input)):
#     if Input[i] > maxn:
#         maxn = Input[i]
#         index = i

# print("Largest:", maxn)
# print("Index:", index)


# 👉 Count the number of vowels in a given string.
# strname ="EYE"
# strname=str.lower(strname)
# vowles="aeiou"
# count=0

# for i in strname:
#     # print(i)
#     if i in vowles:
#         count+=1


# print(count)


#Write a program to reverse  sentence.
# strsentence="how are you?"
# strsentence=reversed(strsentence)
# strsentence="".join(strsentence)
# print(strsentence)
# strwords="oop"
# print(strwords[::-1])
    

#Write a program to reverse the words in a given sentence.


# strsentence = "how are you?"


# words = strsentence.split()



# reversed_words = words[::-1]



# result = " ".join(reversed_words)
# print(result)  

# Write a program to find the GCD (Greatest Common Divisor) of two numbers.


# num1=36
# num2=60
# smallnumber = num1 if num1 < num2 else num2
# emptylist=[]
# for i in range(1,smallnumber+1):
#     if num1%i==0 and num2%i==0:
#         emptylist.append(i)


# print(max(emptylist))


# num1 = 36
# num2 = 60

# smallnumber = num1 if num1 < num2 else num2
# gcd = 1   # store greatest divisor found so far

# for i in range(1, smallnumber + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i   # update gcd

# print("GCD is:", gcd)



# num1 = 36
# num2 = 60

# while num2 != 0:
#     num1, num2 = num2, num1 % num2

# print("GCD is:", num1)


# print(36%60)

# dAY 13
# name="hello"
# name=name.lower()
# print(name == name[::-1])


# 👉 Day 14 Problem: Find the sum of digits of a given number.


# number=1234
# sum=0
# while number > 0:
#         digit = number % 10
#         sum =sum+digit
#         number = number // 10

# print(sum)

# 👉 Day 16 Problem: Write a program to check whether a string is a pangram or not.

# alphabets = "abcdefghijklmnopqrstuvwxyz"
# INPUT_word = "The quick brown fox jumps over the lazy dog"
# INPUT_word=INPUT_word.replace(" ","").lower()
# empty_list=[]

# alphabets=sorted(alphabets)


# for i in INPUT_word:
#     if i not in empty_list:
#         empty_list.append(i)



# print("pangram") if alphabets==(sorted(empty_list)) else print("no")




# alphabets = "abcdefghijklmnopqrstuvwxyz"
# INPUT_word = "The quick brown fox jumps over the lazy dog"

# # Clean input
# INPUT_word = INPUT_word.replace(" ", "").lower()

# # Get unique letters
# letters = set(INPUT_word)

# # Check
# if set(alphabets).issubset(letters):
#     print("pangram")
# else:
#     print("not pangram")

# Write a program to find all prime numbers in a given range.

# start = 10  
# end = 30


# for number in range(start, end+1):
#     count = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             count += 1
#     if count == 2:
#         print(number)



# Check if a number is an Armstrong number



# number=153
# numl=len(str(number))

# sum=0
# while number > 0:
#         digit = number % 10
#         print(digit)
#         sum+=digit**numl
#         number = number // 10
        

# print(sum)


# Reverse the words in a sentence
# Input= "I love Python"


# Input=Input.split()
# Input=Input[::-1]
# Input=" ".join(Input)
# print(Input)

# Find the Largest Element in a List

# Number_list=[22,54,3242,663,22]
# max_number=Number_list[0]

# for i in Number_list:
#     if i>max_number:
#         max_number=i


# print(max_number)


# Find the Smallest Element in a List

# Number_list=[22,54,3242,663,12]
# min_number=Number_list[0]

# for i in Number_list:
#     if i<min_number:
#         min_number=i


# print(min_number)


# Find the Second Smallest Element in a List

# Number_list=[22,54,3242,663,12]
# min_value = min(Number_list)
# Number_list.remove(min_value)
# second_min = min(Number_list)
# print(second_min)


# Find the Missing Number in a List
#  if number is sorted form that time you use this or first do sorting
# S_list = [1, 2, 3, 5]
# small_element = S_list[0]
# print(small_element)
# large_element = S_list[-1]
# print(large_element)
# empty_list = []
# for i in range(small_element, large_element + 1):
#     empty_list.append(i)

# print(empty_list)

# for num in empty_list:
#     if num not in S_list:
#         print(num)


# # if number is unsorted form that time you can use this also
# S_list = [23,22,25,21]
# small_element = (min(S_list))
# print(small_element)
# large_element =(max(S_list))
# print(large_element)
# empty_list = []
# for i in range(small_element, large_element + 1):
#     empty_list.append(i)

# print(empty_list)

# for num in empty_list:
#     if num not in S_list:
#         print(num)



# Remove Duplicates from a List

# Number_list=[1, 2, 2, 3, 4, 4, 5]
# newnumber_list=[]

# for i in Number_list:
#     if i not in newnumber_list:
#         newnumber_list.append(i)


# print(newnumber_list)



# # Find the Intersection of Two Lists

# List1 = [1, 2, 3, 4, 5]
# List2 = [4, 5, 6, 7, 8]

# List1=(set)(List1)
# List2=(set)(List2)
# print(List1,List2)
# result=List1.intersection(List2)
# print(list(result))


# intersection = []
# for i in List1:
#     if i in List2 and i not in intersection:
#         intersection.append(i)
# print(intersection)



# Find the Union of Two Lists

# List1 = [1, 2, 3, 4]
# List2 = [3, 4, 5, 6]

# new_list=[]
# for i in List1:
#     if i not in List2:
#         new_list.append(i)

# print(new_list+List2)

# List1=(set)(List1)
# List2=(set)(List2)
# print(List1,List2)
# result=List1.union(List2)
# print(list(result))



# Find the Difference of Two Lists


# List1 = [1, 2, 3, 4]
# List2 = [3, 4, 5, 6]

# new_list=[]
# for i in List1:
#     if i not in List2:
#         new_list.append(i)

# print(new_list)


# Find the Symmetric Difference Between Two Lists

# List1 = [1, 2, 3, 4]
# List2 = [3, 4, 5, 6]
# list1=set(List1)
# list2=set(List2)
# result=list1.symmetric_difference(list2)
# print(result)

# Check for Palindrome String
# string_sentence= "A man a plan a canal Panama"

# string_sentence=string_sentence.replace(" ","").lower()


# print("True") if string_sentence=="".join(reversed(string_sentence)) else print("F")


# Check if a Number is a Perfect Number

# number=28
# result=0
# for i in range(1,number // 2 + 1):
#     if number%i==0:
#         result+=i

# if result==number:
#     print("prefect")
# else:
#     print("not")


# Check if a Number is a Strong Number







number=145

while number>0:
    number=number%10
    sum_facto=1
    for i in range(1,number+1):
        sum_facto*=i

 
    number=number//2

print(sum_facto)


