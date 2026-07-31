#1
# name="Manthan"
# age=21
# City="Ahmebadab"

# print("My name is",name)
# print("I am",age,"years old")
# print("i am from",City)

#2
# num1=int(input("Enter the first Number\n"))
# num2=int(input("Enter the second number\n"))
# total=num1+num2
# print("sum",total)

#3
# number=int(input("ENTER THE NUMBER\n"))
# if number==0:
#     print("this is zeo")
# elif number%2==0:
#     print("this is even")
# else :
#     print("this is odd")

#4
# num1=int(input("Enter the first Number\n"))
# num2=int(input("Enter the second number\n"))
# if num1>num2:
#     print("num1 is big")
# else :
#     print("num2 is big")

#5
# length=float(input("Enter the length\n"))
# width=float(input("Enter the width\n"))
# area=length*width
# print(area)

#6
# number=int(input("ENTER THE NUMBER\n"))
# i=1
# while i <=10:
#   print(number,"*",i,"=",number*i)
#   i += 1

#7
# total=0
# i=0
# number=int(input("ENTER THE NUMBER\n"))
# while i<=number:
#     total=total+i
#     i=i+1

# print(total)

#8
# vowels=["a","e","i","o","u"]
# word="manthan"
# count=0
# for word in vowels:
#     if(word==vowels):
#         count=count+1

# print(count)

#9
# word=(input("ENTER THE word\n"))
# print("".join(reversed(word)))

#10
# num1=int(input("Enter the first Number\n"))
# op=input("enter operation +,-,*,/n")
# num2=int(input("Enter the second number\n"))
# match op:
#   case "+":
#     print(num1+num2)
#   case "-":
#     print(num1-num2)
#   case "*":
#     print(num1*num2)
#   case "/":
#     print(num1/num2)

#11
# i=0
# numberlist=[]
# while i<5:
#     number=int(input("Enter the Numbers\n"))
#     numberlist.append(number)
#     i=i+1

# print(numberlist)

# print(sum(numberlist))
# sum=(sum(numberlist))
# print(sum/5)

#1

# name=str(input("Enter the Name to convert into the upper case\n"))
# print(name.upper())

#2
# word=(input("Enter the Word\n"))
# print(word.count("a"))

#3
# sentence=(input("Enter the sentence\n"))
# print(sentence.replace("python","java"))

#4
# sentence=(input("Enter the sentence for word count\n"))
# print(len(sentence.split()))

#5
# word=(input("Enter the Word\n"))
# indexfind=input("Enter the charater to find it index\n")
# print(word.find(indexfind))

# lista=[1,2]
# lista.append([3,4])
# print(lista)

#1
# a_list=[1,2,3,4,5]
# print(a_list)

#2
# numbers = [10, 20, 30]
# num=int(input("Enter the number\n"))
# numbers.append(num)
# print(numbers)

#3
# numbers = [10, 20, 30, 40]
# num=int(input("Enter the number\n"))
# numbers.remove(num)
# print(numbers)

#4
# numbers = [45, 12, 78, 3, 56]
# print(max(numbers))
# print(min(numbers))

#5
# numbers = [5, 2, 8, 1, 9]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)


# #1
# a_list=[1,2,3,4]
# print(a_list*2)


#1
# total=0
# number=int(input("Enter the number\n"))
# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#         total+=i
#     i=i+1

# print(total)
    

#2
# words=input("enter the word\n")
# lower=0
# upper=0
# for char in words:
#     if char.isupper():
#         upper+=1
#     else:
#         lower+=1

#3
# numbers = [1,2,2,3,4,4,5]
# not_d=[]
# for num in numbers:
#     if num not in not_d:
#         not_d.append(num)
#     print(num)

# print("hello",not_d)

# #4
# sentence=input("enter the sentence\n")
# # print(sentence)

# sentence=sentence.split()
# # print(sentence[1])
# # print(len(sentence))
# i=1
# bigsen=0
# while(i<len(sentence)):
#     if len(sentence[i]) > bigsen:
#         bigsen=len(sentence[i])
#         i+=1

# print((sentence[bigsen-1]))

#5
# word=input("enter the word\n")
# if word=="".join(reversed(word)):
#     print("Palindrome")
# else:
#     print("not Palindrome")

#6

# user_string = input("Enter a string: ")

# digit_count = 0

# for char in user_string:
#     if char.isdigit():
#         digit_count += 1

# print("Output:", digit_count)


#7
# list1=[1,2,3]
# list2=[4,5,6]

# print(list1+list2)
# list1.extend(list2)
# print(list1)

#8
# numbers = [12,45,7,89,34]
# maxn=(max(numbers))
# n_r=numbers.remove(maxn)
# print(max(numbers))

#10
# name=input("enter student name")
# sub1=int(input("enter first subject marks"))
# sub2=int(input("enter second subject marks"))
# sub3=int(input("enter third subject marks"))

# total=sub1+sub2+sub3
# print(total)
# print(total/3)

# if total/3>=90:
#     print("A")
# elif total/3>=75:
#     print("B")
# elif total/3>=60:
#     print("c")
# else :
#     print("fail")

#1
# numbers_list = []


# while len(numbers_list) < 10:
#     number = int(input("Enter a number: "))
#     numbers_list.append(number)

# print("Your 10 numbers are:", numbers_list)

# odd_num=0
# even_num=0
# zero=0
# for num in numbers_list:
#     if num==0:
#         zero+=1
#     elif num%2==0:
#         even_num+=1
#     else:
#         odd_num+=1

# print(odd_num)
# print(even_num)
# print(zero)

#2

# numbers_list = []

# while len(numbers_list) < 5:
#     number = int(input("Enter a number: "))
#     numbers_list.append(number)

# bign=0
# for i in numbers_list:
#     # print(i)
#     if i>bign:
#         bign=i

# print(numbers_list)
# print(bign)
    
#3
# numbers_list = []

# while len(numbers_list) < 5:
#     number = int(input("Enter a number: "))
#     numbers_list.append(number)

# bign=numbers_list[0]
# for i in numbers_list:
#     # print(i)
#     if i<bign:
#         bign=i

# print(numbers_list)
# print(bign)

#4
# vowels = ["a", "e", "i", "o", "u"]
# word = input("enter the word")
# countv = 0
# countvc = 0

# for char in word:
#     if char in vowels:
#         countv += 1
#     else:
#         countvc += 1

# print(f"Vowels: {countv}")        
# print(f"Consonants: {countvc}") 

#5
# word = input("enter the word\n")
# charatercount=input("enter the charater\n")
# countc=0
# for i in word:
#     print(i)
#     if i==charatercount:
#         countc+=1

# print(countc)

#6
# numbers = [10,20,30,40,50]
# r_number=[]
# i=len(numbers)-1
# while(i>=0):
#     # print(numbers[i])
#     r_number.append(numbers[i])
#     i-=1

# print(r_number)

#7
# sentence = input("Enter your sentence: ")
# print(sentence)
# words = sentence.split()
# print(words)
# result = ''.join(words)
# print(result)

# #8
# numbers = [1,2,2,3,4,4,5]
# not_d=[]
# i=0
# j=1
# while(i<len(numbers)):
#     while(j<len(numbers)):
#         if numbers[i]==numbers[j]:
#             not_d.append(numbers[i])
#             j+=1
#     i+=1

# print("hello",not_d)
# print(numbers)

#9
# numbers_list = []


# while len(numbers_list) < 10:
#     number = int(input("Enter a number: "))
#     numbers_list.append(number)

# print("Your 10 numbers are:", numbers_list)

# p=0
# n=0
# zero=0
# for num in numbers_list:
#     if num==0:
#         zero+=1
#     elif num>0:
#         p+=1
#     else:
#         n+=1

# print(p)
# print(n)
# print(zero)


#10
# numbers_list = []

# name=input("enter the name\n")
# while len(numbers_list) < 5:
#     number = int(input("Enter a number: "))
#     numbers_list.append(number)

# print(max(numbers_list))
# print(min(numbers_list))
# print(sum(numbers_list)/len(numbers_list))

#short

# numbers = [90,0,6,92,42]
# number_empty=[]

# empty_v=0
# # print(numbers[0])
# # print(numbers[1])
# i = 0

# while i < len(numbers):

#     j = i + 1

#     while j < len(numbers):
#         if numbers[i]>numbers[j]:
#             empty_v=numbers[i]
#             numbers[i]=numbers[j]
#             numbers[j]=empty_v

#         # compare numbers[i] and numbers[j]

#         j += 1

#     i += 1

# print(numbers)


#1
# username=input("Enter your username")
# password=input("Enter your password")

# if username=="admin":
    
#     if password=="1234":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("Wrong Username")

#2
# amount=int(input("Enter the Amount you withdraw"))
# pin=int(input("Enter the PIN"))

# Correct_pin=1234
# balance=10000

# if pin==Correct_pin:
#     if amount>balance:
#         print("Insufficient Balance")
#     else:
#         print("Transaction Successful\n""Remaining Balance: ",balance-amount)

# else:
#     print("Invalid PIN")

#3
# marks=int(input("Enter the marks"))
# family_income=int(input("Enter your family income"))

# if marks>=85:
#     if family_income<=300000:
#         print("Scholarship Approved")
#     else:
#         print("Income TOO High")
# else:
#     print("Low Marks")

#4
# Y_O_e=int(input("Enter Your Experinces in years"))
# P_r=int(input("Enter your rating(1-5)"))

# if Y_O_e>=5:
#     if P_r>=4:
#         print("Bonus Approved")
#     else:
#         print("please improve your rating")
# else:
#     print("YOur Experience is too little to get the Bouns")


#5
# mathsm=int(input("Enter your maths marks"))
# engm=int(input("Enter your english marks"))
# age=int(input("enter you age"))

# if age>=17:
#     if mathsm>=60:
#         if engm>=50:
#             print("Admission Approved")
#         else:
#             print("Rejected: English Marks Too Low")
#     else:
#         print("Rejected: Maths Marks Too Low")
# else:
#     print("Rejected: Age Not Eligible")

