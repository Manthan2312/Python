# num1=int(input("Enter the Number\n"))
# num2=int(input("Enter the Number\n"))
# message = "both are zero" if num1 == 0 and num2 == 0 else "both are equals" if num1 == num2 else "num1 is bigger" if num1 > num2 else "num2 is bigger"
# print(message)

# Use elif when checking multiple mutually exclusive conditions.

# Avoid deeply nested if statements when possible; they reduce readability.

# Prefer ternary expressions for simple decisions.


# number=1
# print("even") if number%2==0 else print("odd")


# ternary expressions is a short if else 


names=["Manthan","Khushbu","Tiya","Tirth","Isha","Mahipal","Araya"]
for index,i in enumerate(names):          #BY defualt start with 0 and you can use the start what number or index you want 
    print(index,i)



names=["Manthan","Khushbu","Tiya","Tirth","Isha","Mahipal","Araya"]
for index,i in enumerate(names,start=1):
    print(index,i)
    