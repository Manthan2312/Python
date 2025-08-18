# def is_prime(number):
#     count=0
#     for i in range(1,number+1):
#         if number%i==0:
#             count+=1


#     if(count==2):
#         return True
#     else:
#         return False
    

# def reverse_number(n):
#     rev=0
#     while(n>0):
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10

#     print (rev)


# number=int(input("Enter the number\n"))
# if is_prime(number):
#     print(number,"is a prime number")
# else:
#     print(number,"is not a prime number")
    


# n=int(input("Enter the number\n"))
# reverse_number(n)


# def count_case(s):
#     ucount = 0
#     lcount = 0
#     for i in s:
#         if i.isupper():
#             ucount += 1
#         else:
#             lcount+=1

#     print("The words in uppercase:",ucount)
#     print("The words in lowercase:",lcount)



# s=input("Enter the string\n")
# count_case(s)

# def decimal_part(num):
#     num = str(num)
#     decimal_part = num.split('.')[1]
#     print(decimal_part)


# num=float(input("Enter the float number\n"))
# decimal_part(num)


# def starts_with_vowel_words(sentence):

#     vowels = "aeiouAEIOU"
#     words = sentence.split()
#     result = []

#     for word in words:
#         if word and word[0] in vowels:
#             result.append(word)
    
#     return result
   


# sentence = "Apple is on the orange table under the umbrella"
# vowel_words = starts_with_vowel_words(sentence)
# print("Words that start with a vowel:", vowel_words)



# def armstrogn_number():
#     number = (input("Enter a number: "))
#     numberlen=len(number)
#     number=int(number)

#     original = number  # Keep the original number
#     sum = 0

#     while number > 0:
#         digit = number % 10
#         sum += digit ** numberlen
#         number = number // 10

    
    
#     if original == sum:
#          print("Armstrong number.")
#     else:
#         print("Not an Armstrong number.")


# armstrogn_number()


# def is_perfect():
#     num = int(input("Enter a number: "))
#     sum=0
#     for i in range(1,num):
#         if num % i == 0:
#             sum += i
            
            
            
#     if sum == num:
#         print("Perfect number")
#     else:
#         print("Not a perfect number")

# is_perfect()


# def sum_list(lst):
#     # ls=sum(list)  #this is with help of bulit in function
#       print(ls)
#     total=0
#     for i in lst: #this is thing behind the bulit in function logic
#         total+=i


#     print(total)

# list=[1,2,3,4,5,6]
# sum_list(list)




# def  max_in_list(lst):
#   #  mn=max(list)#this is with help of bulit in function
# #      print(mn)

  
#     maxn = lst[0]  # Assume first element is the largest
#     for i in range(1, len(lst)):
#         if lst[i] > maxn:
#             maxn = lst[i]
#     return maxn

# # Example usage:
# my_list = [3, 9, 4, 1, 711]
# print("Maximum value:", max_in_list(my_list))


# def remove_duplicates(lst):
#     # unique_list = list(set(lst))
#     # print(unique_list)

#     # unique_list = list(dict.fromkeys(lst))
#     # print(unique_list)
#     uni=[]
   
#     for i in lst:
#         if i not in uni:
#            uni.append(i)

#     print(uni)



# list1=[123,45,11,11,43,45,12]
# remove_duplicates(list1)


# def reverse_list(lst):
#     # lst.reverse()
#     # print(lst)
    




#     list=[1,2,3,4,5]
#     reverse_list(list)

# def count_even_odd(lst):

#     even = 0
#     odd = 0
#     for num in lst:
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return (even, odd)



    


# list=[1,2,3,45,4]
# c=count_even_odd(list)
# print(c)


# def find_common(list1, list2):

#     common_elements = list(set(list1) & set(list2))
#     print(common_elements)  # Output: [3, 4]



# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# find_common(list1,list2)



# def square_elements(lst):
#     squared = []
#     for num in lst:
#         squared.append(num ** 2)
#     return squared

# numbers = [2, 3, 4]
# result = square_elements(numbers)
# print("Squared list:", result)




# def get_index(lst, value):
#     if value in lst:
#         return lst.index(value)
#     else:
#         return -1



# number=[1,2,3,4]
# a=get_index(number,1)
# print(a)


# def is_sorted(lst):
#     return lst == sorted(lst)

# list=[6,21,1,45]
# c=is_sorted(list)
# print(c)





# def list_stats(lst):
#     total = sum(lst)
#     avg = total / len(lst)
#     minimum = min(lst)
#     maximum = max(lst)
#     return (total, round(avg, 2), minimum, maximum)


# numbers = [2, 5, 7]
# stats = list_stats(numbers)
# print("Sum:", stats[0])
# print("Average:", stats[1])
# print("Min:", stats[2])
# print("Max:", stats[3])


#Write a function that takes a list of numbers and returns the sum of all even numbers.

# def totalofeven_list(list):
#     total=0
#     for i in list:
#         if(i%2==0):
#             total+=i
    
#     print(total)


# list=[1,2,3,4,5]
# totalofeven_list(list)

# def find_squ(number):
#     return number*number
# number=int(input("Enter the number to find the square\n"))
# ans=find_squ(number)
# print(ans)

# def greeting(name):
#     print("Good Morning",name)
# name=input("Enter the Name\n")
# greeting(name)


# def max_from_three(a,b,c):
#     # ans=max(a,b,c)
#     # print(ans)
#     # if(a>b and a>c):
#     #     print(a)
#     # elif(b>a and b>c):
#     #     print(b)
#     # else:
#     #     print(c)

# num1=int(input("Enter the three numbers\n"))
# num2=int(input())
# num3=int(input())
# max_from_three(num1,num2,num3)


# def factorial(number):
#     ans=1
#     i=1
#     while(i<=number):
#         ans=ans*i
#         i=i+1

#     print(ans)


# number=int(input("enter the number\n"))
# factorial(number)




# def is_even(number):
#     if number%2==0:
#         return True
#     else:
#         return False
    

# n=int(input("Enter the number\n"))
# ans=is_even(n)
# print(ans)



# def res_string(string):

#     string=list(string)
#     string.reverse()
#     string=''.join(string)
#     print(string)


# string=(input("Enter the string\n"))
# res_string(string)



# def number_vowel(string):
#     count=0
#     vo = "aeiou"
#     string=str.lower(string)
#     for i in string:
#         if i in vo:
#             count=count+1

    
#     print(count)




# string=input("enter the string\n")
# number_vowel(string)


# def Fibonacci(number):
#         i=0
#         a=0
#         b=1
#         ans=0
#         while(i<number): 
#             print(a)
           
#             ans=a+b
#             a=b
#             b=ans
#             i=i+1


# number=int(input("Enter the number\n"))
# Fibonacci(number)


# def is_prime(number):
#     count=0
#     for i in range(1,number+1):
#         if number%i==0:
#             count=count+1

  

#     if(count==2):
#         print("It is a prime number\n")
#     else:
#         print("noT A PRIME number\n")




# number=int(input("Enter the number\n"))
# is_prime(number)



def is_sum(list):
   # return sum(list)
    total=0
    for i in list:
        total=total+i

    return total



list=[1,2,3,4,5]
ans=is_sum(list)
print(ans)