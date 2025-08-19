#most of the cases finally keyword used with user defined function 
#When we need to print things after the returning the value 


# def my_function():
#     try:
#         num=int(input("enter the number\n"))
#         return num
#     except:
#         print("An error occurred")
#         return 0
#     finally:
#         print("This is finally block")
#     # return statement is used to return value from function



# print(my_function()) 



# number=int(input("Enter the number between 1 to 100\n"))
# print(number)
# if number<=100 and  number>0:
#     print("number is Valid")
# else:
#     raise ValueError("number is not between 1 to 100") #using the raise keyword we do the throw errors why we throw the errors we learn with this example 

# #there are many cases to raise the errors and 
# s=number*number
# print(s)


# number=int(input("Enter the salary between 40000 to 100000\n"))
# print(number)
# if number < 40000 or number > 100000:
#     raise ValueError("Salary is not between 40000 and 100000")



print("it is work")
    


def function_oe(x):

    try:
        return x % 2 == 0
    finally:
        print("note this is after return")

print(function_oe(2))




