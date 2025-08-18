"""
name="MANTHAN"
age=20
city="BOSTON"
print("My Name is" ,name)
print("I am",age,"years old")
print("I am form",city)


num1=23
num2=5
print("Before swap")
print(num1)
print(num2)
temp=num1
num1=num2
num2=temp
print("After swap")
print(num1)
print(num2)

length=23.1
width=56.2
print("The Area of a rectangle",length*width)


number=int(input("ENTER A NUMBER\n"))
print(number)
if(number==0):
    print("The Number is Zero")
elif(number>0):
    print("The Number Is Positive")
else:
    print("The Number Is Negitive")


age=int(input("Enter the your age\n"))
print(age)
if(age>18):
    print("DO VOTE")
else:
    print("YOU GO TO DO HOMEWORK")


number1=int(input("Enter the Three Numbers\n"))
number2=(int)(input())
number3=(int)(input())
if(number1>number2 and number1>number3):
    print("THE NUMBER1 IS BIG")
elif(number2>number1 and number2>number3):
    print("THE NUMBER2 IS BIG")
elif(number1==number2==number3):
    print("ALL NUMBERS ARE EQUAL")
else:
    print("THE NUMBER3 IS BIG")



for i in range(1,21):
    print(i)

for i in range(1,51):
    if(i%2==0):
        print(i)


i=1
while(i<=50):
    if(i%2==0):
        print(i)
    i+=1
    


Multinu=int(input("Enter the Number\n"))
for i in range(1,11):
    print(Multinu,"*",i,"=",Multinu*i)


for i in range(1,11):
    if(i==5):
        break
    print(i)


i=1
while(i<=10):
    if(i==7):
        i=i+1
        continue
    print(i)
    i=i+1


for i in range(1,11):
    if(i==7):
        continue
    print(i)





string = input("Enter the string:\n")
string = string.lower()
print("The Length Of string is:",len(string))


string1 = "".join(reversed(string))
print(string1)

if string == string1:
    print("The string is palindrome")
else:
    print("The string is not palindrome")



string = input("Enter a string:\n")
string = string.lower()

vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


num1=int(input("Enter the two numbers\n"))
num2=int(input())

print(num1+num2)



# Convert float to int
num1 = float(input("Enter a float number:\n"))
print("Original float:", num1)
print("After converting to int:", int(num1))

# Convert int to float
num2 = int(input("\nEnter an integer number:\n"))
print("Original integer:", num2)
print("After converting to float:", float(num2))



string="Manthan"
number=23
number=str(number)
print(string+number)



Number=int(input("Enter the Number\n"))
match Number:
    case 1:print("one")
    case 2:print("two")
    case 3:print("three")
    case 4:print("four")
    case 5:print("five")
    case _:print("Invalid")


grade=(input("Enter the Grade\n"))
grade=grade.upper()
match grade:
    case "A":print("Excellent")
    case "B":print("Good")
    case "C":print("Average")
    case "D":print("Below Average")
    case "F":print("Fail")
    case _:print("Invalid")
    """
#new day second
"""
principal=1000
rate=10 
time=2
print("THE Simple interest",(1000/10)*2)

name=(input("Enter Your Name\n"))
by=int(input("Enter Your Birth year\n"))

count=0
for i in range(by,2025):
    count+=1
print(name,"You are",count,"Year's old")




name="PUSHPA"
actor="Allu Arjun"
releaseyear=2021

print("My favorite movie is",name,"and",actor,"is the hero of that movie and ReleseYear is",releaseyear)


year=int(input("Enter The Year\n"))
if year%4==0 or year%100==0 or year%400==0:
     print("LEAP YEAR")
else:
    print("Not a Leap Year")


A1=int(input("Enter The three angles of triangle\n"))
A2=int(input())
A3=int(input())
if(A1+A2+A3==180):
    print("Valid Triangle")
else:
    print("Invalid Triangle")



number=int(input("Enter the number\n"))
if(number<0):
    print("NUmber is negitive")
elif(number==0):
    print("Number is zero")
elif(number%2==0):
    print("Number is even")
else:
    print("Number is odd")


number=int(input("Enter the number\n"))
if(number%5==0 & number%11==0):
    print("The Number is Divide By Both")
else:
    print("The Number is not Divide By Both")


number=int(input("Enter The Number\n"))

facto=1
for i in range(1,number+1):
    facto=facto*i

print(facto)

# for i in range(1,51):
number=int(input("Enter The Number\n"))
count=0
for i in range(1,51):
    if(number%i==0):
        count+=1

if(count==2):
    print("Number is prime number")
else:
    print("Number is not prime number")

print("Prime numbers between 1 and 50 are:")

for num in range(1, 51):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num, end=" ")

digit=int(input("Enter the number\n"))
i=0
sum=0
while(i<=digit):
    sum=sum+i
    i+=1
print(sum)

n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
  

for i in range(1,21):
    if(i%13==0):
            exit()
    print(i)
  
for i in range(1,21):
            if(i%2==0):
                print(i)
                continue
           

while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    
    if user_input.lower() == "exit":
        print("Exiting the loop. Goodbye!")
        break

    print("You entered:", user_input)
      

string = input("Enter a string:\n")
string = string.lower()
len=len(string)
print(len)
vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of consonants:", len-count)
 

sentence = input("Enter a sentence:\n")

# Split the sentence by spaces into words
words = sentence.split()

# Count the number of words
print("Number of words:", len(words))


str="act"
str1="cat"
str= str.lower()
str1= str1.lower()

str = "".join(sorted(str))
str1 = "".join(sorted(str1))

if(str==str1):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")


sentences="manthan is a good boy"
words=sentences.replace(" ","-")

print(words)

words=input("Enter the sentence\n")
words=sentences.title()
print(words)

#today 3/7/2025
number1=float(input("Enter the two float numbers\n"))
number2=float(input())

ave=number1+number2/2
ave=(int(ave))
print(ave)


string="45.98"
string=(float(string))
print(type(string))

covertint=string
covertint=int(covertint)
print(type(covertint))



a=int(input("Enter the number\n"))
print("square:",a*a)
print("square:",a*a*a)




number=int(input("Enter The number\n"))
if(number%2==0):
    if(number%3==0):
        print("number is divisible by 2 and 3")
else:
        print("number is not divisible by 2 and 3")



number=int(input("Enter the marks\n"))
if(number>=90):
    print("A grade")
elif(number>=80):
    print("B grade")
elif(number>=70):
    print("C grade")
elif(number>=60):
    print("D grade")
else:
    print("F grade")



mark=(input("Enter the char\n"))
if(mark=="a" or mark=="e" or mark=="i" or mark=="o" or mark=="u"):
        print("vowel")
elif(mark=="!" or mark=="@" or mark=="#" or mark=="$" or mark=="%" or mark=="^" or mark=="&"):
        print("special char")
else:
        print("special character")



n=int(input("Enter the number\n"))

for i in range(1,n+1):
    print("7 * ",i,"=",7*i)



number=int(input("Enter the number\n"))
rev=0
while(number>0):
    digit=number%10
    print("last digit of number is",digit)
    rev=rev*10+digit
    number=number//10
    print("reverse of number is",rev)



evensum=0
oddsum=0
for i in range(1,51):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i


print(evensum)
print(oddsum)


i=10
while(i>=1):
    print(i)
    i=i-1


for i in range(1,100):
        if(i%7==0 and i%11==0):
            break
        print(i)


string = input("Enter a string: ")

vowels = "aeiouAEIOU"

for char in string:
    if char in vowels:
        continue
    print(char, end="")



string="My name is Manthan"
string=string.split(" ")
print(string)



num1=input("Enter the number\n")
num2=input()
num1=float(num1)
num2=float(num2)
multiply=num1*num2
print(multiply)



c=float(input("Enter the tem\n"))
f=c*9/5 + 32
f=round(f,2)
print(f)


hour = int(input("Enter the hours (0-24): "))
minute = int(input("Enter the minutes (0-59): "))

if hour > 24 or hour < 0:
    print("Invalid hour")
    exit()
if minute >= 60 or minute < 0:
    print("Invalid minute")
    exit()

total_seconds = hour * 3600 + minute * 60
print("Total seconds:", total_seconds)




number=int(input("Enter the Number\n"))
if(number%3==0):
    print("Fizz")
elif(number%5==0):
    print("Buzz")
elif(number%3==0 and number%5==0):
    print("FizzBuzz")
else:
    print(number)
 

inp=input("Enter the char\n")

if(len(inp)>1):
    print("This is not a char.(char is only 1 letter)")
    exit()
elif(inp=="1" or inp=="2" or inp=="3" or inp=="4" or inp=="5" or inp=="6" or inp=="7" or inp=="8" or inp=="9" or inp=="0" ):
    print("Digit")
elif(inp=="!" or inp=="@" or inp=="#" or inp=="$" or inp=="%" or inp=="^" or inp=="&"):
    print("Special Char")
else:
    print("Alphabet")
      


sum=0
i=1
while(i<=100):
    if(i%2!=0):
        sum=sum+i
        print(i)
    i=i+1

print(sum)
      

number=int(input("Enter the Number\n"))
rev=0
while(number>0):
    digit=number%10
    print("last digit of number is",digit)
    rev=rev*10+digit
    number=number//10
    print("reverse of number is",rev)

if(number==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")
    
number=123458549
imax=max(int(digit) for digit in str(number))
print(imax)



for i in range(1, 5):  # rows: 1 to 4
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



while True:
    num = int(input("Enter a number: "))
    if num <0:
        exit()
 

for i in range(1,21):
    if(i%3==0 or i%5==0):
        continue
    else:
        print(i)
 


number=int(input("Enter the Number\n"))
original=number

sum=0
while(number>0):
    digit=number%10

    number=number//10
 
    sum=digit*digit*digit+sum
  
print(sum)


if(original==sum):
    print( "Armstrong number.")
else:
    print("Not a Armstrong number.")

number = int(input("Enter the number:\n"))

print("Factors (excluding 1 and itself):")
has_factors = False

for i in range(2, number):  # start from 2, skip 1 and the number itself
    if number % i == 0:
        print(i)
        has_factors = True

if not has_factors:
    print("No factors found. It's a prime number.")
"""
print(12/9)
#number=int(input("Enter the number\n"))


print((12//2)*(2))