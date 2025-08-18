
# try:
#     number=int(input("Enter the number\n"))
#     print(f"The Number Entered By The User is {number}")
# except Exception as e:
#     print("Invalid input")
#     print(e)



try:
    num = int(input("Enter a number: "))
    divisor=int(input("Enter a number for divisor: "))
    result=num/divisor
    print(f"{result}\n")
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)