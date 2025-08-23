# # A decorator function
# def my_decorator(func):
#     print("Good morning")
#     return func

# # Apply decorator
# @my_decorator
# def say_hello():
#     print("Hello, World!")

# # Call the function
# say_hello()






# def my_decorator1(func):
  
#     def newf(*args,**kwargs):
#         print("Good morning")
#         func(*args,**kwargs)
#         print("Thank you for using me")

#     return newf

# # Apply decorator
# @my_decorator1
# def say_hello1():
#     print("Hello, World!")

# @my_decorator1
# def add(a,b):
#    print(a+b)

# # Call the function
# say_hello1()
# add(1,2)



# def greet(FN):
#     print("Hello world")
#     # FN()
#     print("Function is compeletd it's task")
#     return FN

    

# @greet
# def function_example():
#     print("WHAT IS THE WAY TO DO THE FUCKING THINGS")


# function_example()



def greet(fn):
    print("You are using the things")
    fn()
    print("Thanks you user")
    return fn


@greet
def calcualter():
    print("Enter the choose")
    print("1.+")
    print("2.-")
    print("3.*")
    print("4./")
    print("5.%")
    choose=int(input("Enter The input as a number\n"))
    # print(choose)
    a=int(input("Enter the Number 1\n"))
    b=int(input("Enter the Number 2\n"))

    match choose:
        case 1:
            print(a+b)
        case 2:
            print(a-b)
        case 3:
            print(a*b)
        case 4:
            print(a/b)
        case 5:
            print(a%b)
        case __:
            print("invalid input")
        



calcualter


