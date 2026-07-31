#1
# for i in range(1,21):
#     print(i)

#2
# number=int(input("Enter your number\n"))
# total=0
# for i in range(number+1):
#     total+=i

# print(total)

#3
# number=int(input("Enter your number\n"))
# for i in range(1,number+1):
#     if i%2==0:
#         print(i)

#4
# word="Programming"
# vowels=["a","e","i","o","u"]
# count_v=0
# for char in word:
#     if char.lower() in vowels:
#         count_v+=1

# print(count_v)

#5
# numbers = [12,45,7,89,23]
# ln=numbers[0]

# for num in numbers:
#     if num>ln:
#         ln=num

# print(ln)

#6
# numbers = [-5,8,10,-2,0,4]
# countp=0
# for num in numbers:
#     if num>0:
#         countp+=1

# print(countp)

#7
# s = "Python"
# rev = ""
# for ch in s:
#     rev = ch + rev
#     print(rev)

# print(rev)
# #8
# word="banana"
# word_l=list(word)
# count_w=0
# count_l={}
# for i in word_l:
#     if i.count("a"):
#         count_w+=1

# print(count_w)

#9
# number=int(input("Enter the number"))
# for i in range(1,11):
#     print(number,"*",i,"=",number*i)

#10
# sales = [1200,1500,1800,900,2200]

# totals=0
# for sale in sales:
#     totals+=sale

# print(totals)

# print("AVE SALE",totals/len(sales))

# bs=sales[0]
# for i in sales:
#     if i>bs:
#         bs=i

# print("Highest sale:",bs)

# ls=sales[0]
# for j in sales:
#     if j<bs:
#         ls=j

# print("lowest sale:",ls)

#Bonus Challenge

# numbers = [45,12,89,67,89,21,56]

# b_number=numbers[0]

# for num in numbers:
#     if num>b_number:
#         b_number=num

# print(b_number)

# b_number=numbers[0]
# new_list=[]
# for num in numbers:
#     if num>b_number:
#         b_number=num
#         new_list.append(num)
#         numbers.remove(num)

# print(numbers)

# s_n=numbers[0]
# for nums in numbers:
#     if b_number==nums:
#         numbers.remove(nums)
#         print(numbers)

# for num in numbers:
#     if num>s_n:
#         s_n=num



# print(b_number)

# print(s_n)

#important

# numbers = [67, 12, 89, 45, 211, 56]
# numbers = [45, 89, 90]
# numbers=[10, 50, 80]

# f_l=numbers[0]
# s_l=numbers[0]
# for i in numbers:
#     if i>f_l:
#         s_l=f_l
#         f_l=i
#     else:
#         if i>s_l and i!=f_l:
#             s_l=i


# print(f_l)
# print(s_l)


# numbers=[30,20,10]

# numbers=sorted(numbers)
# # print(numbers)
# f_l=numbers[0]
# s_l=numbers[0]
# t_l=numbers[0]




# for i in numbers:
#     if i>f_l:
#         s_l=f_l
#         f_l=i
#     else:
#         if i>s_l and i!=f_l:
#             t_l=s_l
#             s_l=i


# print(f_l)
# print(s_l)  
# print(t_l)

# Next Challenge (Data Analytics Style)
# sales = [1200, 1500, 900, 2200, 1800, 2200, 950]
# total_sale=0
# highest_sale=sales[0]
# lowest_sale=sales[0]
# count_s=0
# for i in sales:
#     total_sale+=i
#     if i>highest_sale:
#         highest_sale=i
#     if i<lowest_sale:
#         lowest_sale=i
#     if i>1500:
#         count_s+=1

    
# print(total_sale)
# print(total_sale/len(sales))
# print(highest_sale)
# print(lowest_sale)
# print(count_s)

#1
# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)

#2
# numbers = [10, -5, 20, -3, 15, -8]
# for num in numbers:
#     if num<=0:
#         continue
#     print(num)

#3
# numbers = [10, -5, 20, -3, 15]
# p_t=0
# for num in numbers:
#     if num<=0:
#         continue
#     p_t+=num

# print(p_t)

#4
# names = ["Manthan", "", "Rahul", "", "Neha"]
# for name in names:
#     if name=="":
#         continue
#     print(name)

#5
# marks = [90, -1, 85, 0, 76, 100]
# count_p=0
# for mark in marks:
#     if mark<=0:
#         continue
#     count_p+=1

# print(count_p)

#Bonus (Interview + Data Analytics)
# sales = [1200, 0, -100, 1500, 1800, -50, 2200]

# total_valid_sale=0
# count_valie_sale=0

# for sale in sales:
#     if sale<=0:
#         continue
#     total_valid_sale+=sale
#     count_valie_sale+=1



# print(total_valid_sale)
# print(count_valie_sale)
# print(total_valid_sale/count_valie_sale)

#1
# def display_name():
#     print("My name is Manthan")

# display_name()
# display_name()
# display_name()

#2
# def greet(name):
#     print("Hello",name)

# greet("Manthan")
# greet("Rahul")
# greet("Neha")

#3 
# def square(number):
#     print(number*number)

# square(5)
# square(8)
    
#4
# def student(name, age):
#     print("Name:",name)
#     print("Age:",age)

# student("Manthan",21)
# student("Amit",22)
# student("Tirth",20)

#5
# def table(number):
#     for i in range(1,11):
#         print(number,"*",i,"=",number*i)

# table(5)

#Bonus Challenge
# def analyze(numbers):

#     total = 0
#     count = 0
#     highest = None
#     lowest = None

#     for num in numbers:

#         if num <= 0:
#             continue

#         total += num
#         count += 1

#         if highest is None or num > highest:
#             highest = num

#         if lowest is None or num < lowest:
#             lowest = num

#     if count == 0:
#         print("No positive numbers found.")
#         return

#     print("Total Positive =", total)
#     print("Count Positive =", count)
#     print("Average =", total / count)
#     print("Highest =", highest)
#     print("Lowest =", lowest)


# numbers = [10, 20, -5, 30, 0, 15]

# analyze(numbers)

# numbers_list=[100,32,45,64,22,78]

# large_number=numbers_list[0]
# second_l_n=numbers_list[0]

# for num in numbers_list:

#     if num>large_number:

#         second_l_n=large_number
#         large_number=num

#     if num<large_number and num!=large_number:

#         second_l_n=num

# print(large_number)
# print(second_l_n)

#1
# company = "Google"

# def wordp():
#     print(company)

# wordp()

#2
# country = "India"
# def con():
#     country = "USA"
#     print(country)

# con()
# print(country)

#3
# count=0
# def inc():
#     global count
#     count+=1
#     return count

# print(inc())

#4
# count=0
# def inc():
#     count=0
#     count+=1
#     return count

# print(inc())

#1
# def welcome(name="Guest"):
#     print(name)

# welcome()
# welcome("MANTHAN")

#2
# def area(length, width=10):
#     return length*width

# print(area(5))

#3
# def employee(name, salary=25000):
#     print("employee name",name,"employee salary",salary)

# employee("manthan")
# employee("rahul",23000)

# def analyze(numbers, ignore_negative=True):
#     total=0
#     count=0
#     for num in numbers:
#         if num>0:
#             ignore_negative=False
#             total+=num
#             count+=1
#     return total,count

# numbers=[3,42,654,78,11,-5]

# print(analyze(numbers))
    
    

#1
# def student(name, age):
#     print(name,age)

# student(name="Manthan",age=21)

#2
# def employee(name, salary, city):
#     print(name,salary,city)

# employee(city="SURAT",name="MANTHAN",salary=23000)

#3
# def rectangle(length, width=10):
#     return length*width

# print(rectangle(5))
# print(rectangle(width=20, length=5))

#bouns
# def analyze(numbers, ignore_negative=True):
#     countp=0
#     for num in numbers:
#         if ignore_negative==True and num>0:
#             countp+=1
#         if ignore_negative==False :
#             countp+=1
#     return countp

# numbers=[2,345,245,535,55,-12]
# print(analyze(numbers, ignore_negative=False))
# print(analyze(numbers))

#1
# def total(*numbers):
#     total=0
#     for num in numbers:
#         total+=num

#     return  total

# print(total(10, 20, 30))

#2
# def largest(*numbers):
#     largest_number=0
#     for num in numbers:
#         if num>largest_number:
#             largest_number=num
#     return largest_number

# print(largest(45, 12, 89, 34))

#3
# def average(*numbers):
#     count=0
#     total=0
#     for num in numbers:
#         if num>0:
#             count+=1
#             total+=num
#     return total/count
   

# print(average(1,2,3,4,5,-6))

#4
# def count_even(*numbers):
#     count_even_number=0
#     for num in numbers:
#         if num%2==0:
#             count_even_number+=1
#     return count_even_number

# print(count_even(1, 2, 4, 7, 8))

#bouns
# def analyze(*sales):
#     total_sale=0
#     count_sale=0
#     highest_sale=None
#     lowest_sale=None
#     for sale in sales:
#         if sale>0:
#             total_sale+=sale
#             count_sale+=1
    
#         if highest_sale is None or sale>highest_sale:
#             highest_sale=sale

#         if lowest_sale is None or sale<lowest_sale:
#             lowest_sale=sale

#     return total_sale/count_sale,highest_sale,lowest_sale

# print(analyze(1,2,3,4,5))

#1             
# def student(**details):
#     print(details)

# student(name="Manthan", age=21)

# #2
# def student(**details):
#     print("Name:",details["name"])
#     print("Age:",details["age"])

# student(name="Manthan", age=21)

#3
# def studentdetails(**sdetails):
#     for key,value in sdetails.items():
#         print(key,value)

# studentdetails(name="Manthan", age=21)
# studentdetails(name="ved",age=20)

#4
# def employee(**details):
#     for key,value in details.items():
#         print(key,value)

# employee(
#     name="Rahul",
#     salary=40000,
#     city="Surat"
# )

# #bouns
# def analyze(**data):
#         for key,value in data.items():
#             print(key,":",value)

# analyze(
#     sales=25000,
#     profit=5000,
#     employees=20
# )

#1
# square=lambda x:x*x
# print(square(6))

#2
# add=lambda a,b:a+b
# print(add(10, 20))

#3
# is_positive=lambda x: x>0
# print(is_positive(-5))

#4
# largest = lambda a, b: print("a is big") if a > b else print("b is big")
# print(largest(20, 15))

#5
# sales = [1200, 1500, 1800]
# increase = lambda sale: sale * 1.10

# print(increase(1200))

#1
# try:
#     number=int(input("Enter thr number\n"))
#     print(100/number)
# except ZeroDivisionError:
#     print("error")

#2
# try:
#     number=int(input("Enter thr number\n"))
#     print(number)
# except ValueError:
#     print("error")

#3
# try:
#     number=int(input("Enter thr number\n"))
#     print(number)
# except ValueError:
#     print("invalid input")
# else:
#     print("valid input")

#4
# try:
#     number=int(input("Enter thr number\n"))
#     print(100/number)
# except ZeroDivisionError:
#     print("error")
# finally:
#     print("Program Ended")

#bonus
# numbers = [10, 20, 30]
# try:
#     index_number=int(input("enter the index number\n"))
#     print(numbers[index_number])
# except ValueError:
#     print("invalid datatype")
# except IndexError:
#     print("index error")



#1
# try:
#     with open("notes.txt","w") as file:
#         file.write("Python\nData Analytics")
# except FileNotFoundError:
#     print("File is not found")

#2
# try:
#     with open("notes.txt","a") as file:
#         file.write("\nMachine Learning")
# except FileNotFoundError:
#     print("file not found")

#3
# try:
#     with open("notes.txt","r") as file:
#         data_read=file.read()
#         print(data_read)
# except FileNotFoundError:
#     print("file not found")

#4
# try:
#     with open("notes.txt","r") as file:
#         for i in file:
#             print(i.strip())
# except FileNotFoundError:
#     print("file not found")

#bonus
# sales_number=[]
# try:
#     with open("sales.txt","r") as file:
#         for line in file:
#             print(line.strip())
#             sales_number.append(int(line))
# except FileNotFoundError:
#      print("file not found")           


# print(sales_number)
# total=0
# count=0
# high=None
# low=None
# for sale in sales_number:
  
#     if sale>0:
#         total+=sale
#         count+=1
#     if high is None or sale>high:
#         high=sale
#     if low is None or sale<low:
#         low=sale

# print(total)
# print(total/count)
# print(high)
# print(low)

#1
# class student:
#     pass

# s1=student()
# print(s1)

#2
# class student:

#     def __init__(self,name,age):
#         self.name= name
#         self.age=age
#         print(self.name)
#         print(self.age)

# s1=student("Manthan",21)


#3
# class student:

#     def __init__(self,name):
#         self.name= name
#     def greet(self):
#         print("Hello",self.name)
        

# s1=student("Parth")
# s1.greet()

#4

# class Employee:
    
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(self.name)
#         print(self.salary)

# s1=Employee("Manthan",21000)
# s2=Employee("Man",24000)

#bonus
# class SalesReport():

#     def __init__(self,total_sales,total_orders):
#         self.total_sales=total_sales
#         self.total_orders=total_orders

#     def average_sale(self):
#         return self.total_sales / self.total_orders
    
# report = SalesReport(25000, 50)

# print(report.average_sale())


        
        
    
        
