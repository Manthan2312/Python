# def double(x):
#     return x*2
#above is the normal process to write a function 

#lambada function

double= lambda x:x*2

name=lambda n:print(f"hello, {n}")


print(double(2))
name("Manthan Patel")


max_num = lambda a, b: a if a > b else b
print(max_num(10, 25))  # 25



num1=12 
num2=15


# print(num1 if num1 > num2 else num2)
print(num1 if num1%2==0  else num2)
print("even") if num2%2==0 else print("odd")

