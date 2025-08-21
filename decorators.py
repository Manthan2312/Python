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






def my_decorator1(func):
  
    def newf(*args,**kwargs):
        print("Good morning")
        func(*args,**kwargs)
        print("Thank you for using me")

    return newf

# Apply decorator
@my_decorator1
def say_hello1():
    print("Hello, World!")

@my_decorator1
def add(a,b):
   print(a+b)

# Call the function
say_hello1()
add(1,2)

