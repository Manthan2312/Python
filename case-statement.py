"""
num1=(int)(input("Enter Number 1\n"))
num2=(int)(input("Enter Number 2\n"))
operator=(input("Enter Arthimetic Operator\n"))

match operator:
    case "+":print(num1+num2)
    case "-":(num1-num2)
    case "*":(num1*num2)
    case "/":(num1/num2)
    case "%":(num1%num2)
    case "**":(num1**num2)
    case _:print("Not arthimetic operator")

"""
# number=(int)(input("Enter Your Day\n"))
# print(number)
# match number:
#     case 1:print("Monday")
#     case 2:print("Tuesday")
#     case 3:print("Wednesday")
#     case 4:print("Thursday")
#     case 5:print("Friday")
#     case 6:print("Saturday")
#     case 7:print("Sunday")
#     case _:print("Invalid Day")

# month =(input("ENTER THE MONTH\n")).strip()
# month=month.lower()
# match month:
#     case "1"|"january":
#         print("31")
#     case "2"|"february":
#         print("28 or 29 ")
#     case "3"|"march":
#         print("31")
#     case "4"|"April":
#         print("30")
#     case "5"|"may":
#         print("31")
#     case "6"|"june":
#         print("30")
#     case "7" | "july":
#         print("July has 31 days")
#     case "8" | "august":
#         print("August has 31 days")
#     case "9" | "september":
#         print("September has 30 days")
#     case "10" | "october":
#         print("October has 31 days")
#     case "11" | "november":
#         print("November has 30 days")
#     case "12" | "december":
#         print("December has 31 days")
#     case _:
#         print("Invalid month input")

# print("1.RED")
# print("2.GREEN")    
# print("3.YELLOW")
# number=(input)("Enter your color or number\n").strip()
# number=number.lower()
# match number:
#     case "1"|"red":
#         print("STOP ON RED LIGHT")
#     case "2"|"green":
#         print("GO ON GREEN LIGHT")
#     case "3"|"yellow":
#         print("PREPARE TO STOP ON YELLOW LIGHT")
#     case _:
#         print("Invalid color or number input")


# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# choice=int(input("Enter your choice (1/2/3/4): "))
# match choice:
#     case 1:print("The sum is",number1+number2)
#     case 2:print("The Substraction is",number1-number2)
#     case 3:print("The Multiplication is",number1*number2)
#     case 4:print("The Divison is",number1/number2)
#     case _:print("invalied operation number")

grade=(input)("Enter the grade\n").strip()
grade=grade.lower()
match grade:
    case "a":
        print("91 TO 100")
    case "b":
        print("75 TO 90")
    case "c":
        print("60 TO 74")
    case "d":
        print("40 TO 59")
    case _:
        print("ENJOY OR LIFE")



