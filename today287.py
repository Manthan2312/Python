# a=5
# b=23

# temp=a
# a=b
# b=temp

# print(a)
# print(b)


# name=input("Enter the Name\n")
# age=int(input("Enter the Age\n"))

# print(f"Welcome,{name} Thank You TO Told Us You are {age} Years Old")



# number=int(input("Enter the Number\n"))
# if number==0:
#     print("Zero")
# elif number>0:
#     print("positive")
# else:
#     print("Negative")


# c=float(input("Enter the temperature in Celsius\n"))

# F = (c * 9/5) + 32
# print(F)


# radius=int(input("Enter the Circle radius\n"))
# area=3.14*radius*radius
# print(area)


# number1=int(input("Enter the Number 1\n"))
# number2=int(input("Enter the Number 2\n"))
# choose=("Enter your arthimetic Operation\n")
# choose=input(choose)
# match choose:
#     case "+":
#         print(number1+number2)
#     case "-":
#         print(number1-number2)
#     case "*":
#         print(number1*number2)
#     case "/":
#         print(number1/number2)
#     case __:
#         print("Invalid Operation")



# a=12
# print(type(a))

# b=23.5
# print(type(b))

# c=[21,12]
# print(type(c))

# d=(232,131)
# print(type(d))

# e={324,464}
# print(type(e))

# g="l"
# print(type(g))


# str1="Manthan"
# str2="Man"
# if str1==str2:
#     print("Strings are Equal")
# else:
#     print("Strings are not Equal")


# number1=float(input("Enter the Number1\n"))
# number2=float(input("Enter the Number2\n"))
# sum=number1+number2
# avg=sum/2
# print("Average of the two numbers is",avg)


# num=int(input("Enter the Number\n"))
# if num==0:
#     print("Number is Zero")
# elif num%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")



# for i in range(1,51):
#     print(i)


# num=float(input("Enter the Number to print mulitplication Table\n"))

# for i in range(1,11):
#     print(num,"x",i,"=",num*i) 



# i=1
# sum=0
# while(i<=10):
#     sum=sum+i
#     i=i+1

# print(sum)


# list1=[12,4,5,21,34]

# for i in list1:
#     if i%7==0:
#         break

#     print(i)  # prints each element in the list


# year = int(input("Enter The Year to check if it is a leap year or not\n"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# num1=int(input("Enter the First number\n"))
# num2=int(input("Enter the second number\n"))
# num3=int(input("Enter the third Number\n"))
# if num1==0 and num2==0 and num3== 0:
#     print("All numbers are Zero")
# elif num1==num2==num3:
#     print("All numbers are equal")
# elif num1>num2 and num1>num3:
#     print("Number1 is Big")
# elif num2>num1 and num2>num3:
#     print("Number2 is Big")
# else:
#     print("Number3 is Big")


# pr=float(input("enter your pr\n"))
# if pr>=90:
#     print("Grade A")
# elif pr<90 and pr>=80:
#     print("Grade B")
# elif pr<80 and pr>=70:
#     print("Grade C")
# else:
#     print("Grade F")


# num=float(input("Enter the number to check is divided by 3 and 5\n"))
# if num%3==0 and num%5==0:
#     print("Number is divisible by 3 and 5")
# else:
#     print("Number is not divisible by 3 and 5")



# strv="aeiou"
# char="A"
# char=char.lower()

# for i in char:
#     if i in strv:
#         print("Vowel")


# def factorial(num):
#     i=1
#     facto=1
#     while(i<=num):
#         facto=facto*i
#         i=i+1

#     return facto


# num=float(input("Enter The number to find thier factorial\n"))
# save=factorial(num)
# print("Factorial of",num,"is",save)


# def ns(num):
#     return num*num

# nm=2
# print(ns(nm))



# def isprime(num):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         return True
#     else:
#         return False
    

# num=11
# print(isprime(num))


# def sr(string):
#     return string[::-1]


# string="Hello"
# print(sr(string))



# def suml(list1):
#     sum1=0
#     for i in list1:
#         sum1+=i
#     return sum1
    


# lis=[1,2,3,4,5]
# print(suml(lis))

# Write a Python program to swap two variables without using a third variable.


# a=100
# b=20

# a=a+b
# b=a-b
# a=a-b

# print(a)
# print(b)

# Take a number as input and check if it’s even or odd.

# number=int(input("Enter the Number\n"))
# if number%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")

# Given a string, count how many vowels are in it.

# name="eye"
# volwes="aeiou"
# count=0
# name=str.lower(name)
# for i in name:
#     if i in volwes:
#         count+=1


# print(count)

# Reverse a string without using slicing ([::-1]).


# name="Manthan"

# name=reversed(name)
# name="".join(name)
# print(name)


# Write a Python program to check whether a number is prime.


# count=0
# number=int(input("Enter the number\n"))
# for i in range(1,number+1):
#     if number%i==0:
#         count+=1

# if count==2:
#     print(number,"is a prime number")
# else:
#     print(number,"is not a prime number")


# Write a program to demonstrate:

# in / not in operators


# list_studentname=["Manthan","Khushbu","Tirth","Tiya","Himesh","Arya"]


# if "khushbu" in list_studentname:
#     print("in the list")
# else:
#     print("not in the list")


# if "Manthan" not in list_studentname:
#     print("not in the list")
# else:
#     print("in the list")


# is / is not operators
# a=[1,2,3]
# b=a
# c=[1,2,3]
# print(id(a))
# print(id(b))
# print(id(c))

# if a is b:
#     print("True")


# if b is c or a is c:
#     print("True")
# else:
#     print("False")


# # To check equality of values, use '=='
# if a == c:
#     print("a and c have the same values but are different objects.")








