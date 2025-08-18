import math
def ispalindrome(a):
    a=a.lower()
    print(str(a) == str(a)[::-1])


string="Madam"
ispalindrome(string)


def greet():
    print("Hello")

greet()

def greet(name):
    print("Hello",name)

name="Patel"

greet(name)


def sum(a,b):
    print(a+b)

sum(12,12)


def gmean(a,b):
    mean=math.sqrt(a*b)
    print(mean)


gmean(9,8)
